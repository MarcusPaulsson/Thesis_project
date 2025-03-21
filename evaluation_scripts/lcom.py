import ast
import itertools
import os
import re  # Import the regular expression module

# Define the target Python file to evaluate
TARGET_FILE = "target.py"  # Change this to your desired file name

class LCOMCalculator(ast.NodeVisitor):
    """
    This AST NodeVisitor collects classes and their methods,
    and for each method records the set of instance variables (attributes)
    accessed on 'self'. This implements the basis for calculating the 
    Lack of Cohesion in Methods (LCOM) as defined by Chidamber and Kemerer.

    For a given class, let:
      A(m_i) = set of instance variables that method m_i uses.
    
    Then, let:
      P = { (m_i, m_j) | A(m_i) ∩ A(m_j) = ∅ }  (non-cohesive pairs)
      Q = { (m_i, m_j) | A(m_i) ∩ A(m_j) ≠ ∅ }  (cohesive pairs)
    
    The LCOM is defined as:
      LCOM = |P| - |Q|, if |P| > |Q|
             0,          otherwise.
    """
    def __init__(self):
        # Stores class data: { class_name: { method_name: set(attributes) } }
        self.classes = {}

    def visit_ClassDef(self, node):
        methods = {}
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                # Consider only methods that have at least one argument (typically 'self')
                if child.args.args:
                    method_name = child.name
                    attributes = self._get_used_attributes(child)
                    methods[method_name] = attributes
        self.classes[node.name] = methods
        self.generic_visit(node)

    def _get_used_attributes(self, node):
        """
        Walk through a function/method node and collect the names of attributes
        accessed on 'self'. For example, self.attr is recorded as 'attr'.
        """
        attrs = set()
        for child in ast.walk(node):
            if isinstance(child, ast.Attribute):
                if isinstance(child.value, ast.Name) and child.value.id == 'self':
                    attrs.add(child.attr)
        return attrs

def calculate_lcom(methods):
    """
    Calculate the Chidamber and Kemerer LCOM for a dictionary of methods:
      - methods: { method_name: set(attributes_used) }
    
    Computes:
      P = set of pairs (m_i, m_j) where A(m_i) ∩ A(m_j) = ∅,
      Q = set of pairs (m_i, m_j) where A(m_i) ∩ A(m_j) ≠ ∅.
    
    Returns a tuple: (LCOM, P, Q)
      where LCOM = |P| - |Q| if |P| > |Q|, otherwise 0.
    """
    method_names = list(methods.keys())
    num_methods = len(method_names)
    if num_methods < 2:
        return 0, set(), set()

    non_cohesive_pairs = set()  # P
    cohesive_pairs = set()      # Q

    for m1, m2 in itertools.combinations(method_names, 2):
        attrs1 = methods[m1]
        attrs2 = methods[m2]
        if attrs1.intersection(attrs2):
            cohesive_pairs.add((m1, m2))
        else:
            non_cohesive_pairs.add((m1, m2))

    lcom = len(non_cohesive_pairs) - len(cohesive_pairs)
    if lcom <= 0:
        lcom = 0

    return lcom, non_cohesive_pairs, cohesive_pairs

def analyze_file(filename):
    """
    Parses the specified Python file and computes the LCOM value along with
    sets P and Q for each class.
    Returns a dictionary mapping class names to a tuple (LCOM, P, Q).
    Handles syntax errors gracefully.
    """
    if not os.path.isfile(filename):
        print(f"File '{filename}' not found.")
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)
        calculator = LCOMCalculator()
        calculator.visit(tree)

        results = {}
        for class_name, methods in calculator.classes.items():
            results[class_name] = calculate_lcom(methods)
        return results
    except SyntaxError as e:
        print(f"Syntax error in file '{filename}': {e}")
        return {"ERROR": ("Syntax Error", set(), set())}
    except Exception as e:
        print(f"Error analyzing file '{filename}': {e}")
        return {"ERROR": ("Analysis Error", set(), set())}

def main():
    """
    Analyzes Python files across different model outputs and prompting strategies,
    calculating and comparing LCOM metrics between ChatGPT and Gemini outputs.
    Handles errors gracefully and continues processing remaining files.
    Prints a formatted table with clear headers for each prompt technique.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    results_dir = os.path.join(parent_dir, "results")
    
    # Define models and prompting strategies
    models = ["ChatGPT", "Gemini"]
    strategies = ["Zero-shot", "Zero-shot-CoT", "Expert-role", "Student-role"]
    
    # Dictionary to store file paths
    model_files = {
        model: {
            strategy: {} for strategy in strategies
        } for model in models
    }
    
    # Collect all files
    for model in models:
        for strategy in strategies:
            model_dir = os.path.join(results_dir, model, "cli_games", strategy)
            try:
                files = sorted([f for f in os.listdir(model_dir) if f.endswith(".py")])
                # Store full paths to files
                model_files[model][strategy] = {
                    f: os.path.join(model_dir, f) for f in files
                }
            except FileNotFoundError:
                print(f"Directory not found: {model_dir}")
                model_files[model][strategy] = {}
    
    # Sort files by numerical value in the filename
    def numerical_sort_key(filename):
        match = re.search(r'code_(\d+)\.py', filename)
        return int(match.group(1)) if match else float('inf')
    
    # Process files by strategy
    for strategy in strategies:
        # Get all files for this strategy
        strategy_files = set()
        for model in models:
            strategy_files.update(model_files[model][strategy].keys())
        
        # Skip if no files for this strategy
        if not strategy_files:
            continue
            
        strategy_files = sorted(strategy_files, key=numerical_sort_key)
        
        # Print header for this strategy
        print("\n" + "-" * 120)
        print(f"{'File':<15} {'Strategy':<15} {'ChatGPT LCOM':<40} {'Gemini LCOM':<40}")
        print("-" * 120)
        
        for file_name in strategy_files:
            # Get file paths for both models
            chatgpt_path = model_files["ChatGPT"][strategy].get(file_name)
            gemini_path = model_files["Gemini"][strategy].get(file_name)
            
            chatgpt_results = {}
            gemini_results = {}
            
            # Analyze files if they exist
            if chatgpt_path:
                try:
                    chatgpt_results = analyze_file(chatgpt_path)
                except Exception as e:
                    print(f"Error analyzing {chatgpt_path}: {e}")
                    chatgpt_results = {"ERROR": ("Error", set(), set())}
            
            if gemini_path:
                try:
                    gemini_results = analyze_file(gemini_path)
                except Exception as e:
                    print(f"Error analyzing {gemini_path}: {e}")
                    gemini_results = {"ERROR": ("Error", set(), set())}
            
            # Skip if both files don't exist or failed to analyze
            if (not chatgpt_path or "ERROR" in chatgpt_results) and (not gemini_path or "ERROR" in gemini_results):
                continue
                
            # Get union of class names, excluding ERROR entries
            all_classes = sorted(set(
                [k for k in chatgpt_results.keys() if k != "ERROR"] + 
                [k for k in gemini_results.keys() if k != "ERROR"]
            ))
            
            # Print results
            for i, class_name in enumerate(all_classes):
                chatgpt_lcom = chatgpt_results.get(class_name, ("N/A",))[0]
                gemini_lcom = gemini_results.get(class_name, ("N/A",))[0]
                
                if i == 0:  # First class for this file
                    print(f"{file_name:<15} {strategy:<15} "
                          f"{f'{class_name}: {chatgpt_lcom}':<40} "
                          f"{f'{class_name}: {gemini_lcom}':<40}")
                else:  # Additional classes
                    print(f"{'':<30} {f'{class_name}: {chatgpt_lcom}':<40} "
                          f"{f'{class_name}: {gemini_lcom}':<40}")

if __name__ == "__main__":
    main()