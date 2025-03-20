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
    """
    if not os.path.isfile(filename):
        print(f"File '{filename}' not found.")
        return {}

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    calculator = LCOMCalculator()
    calculator.visit(tree)

    results = {}
    for class_name, methods in calculator.classes.items():
        results[class_name] = calculate_lcom(methods)
    return results

def main():
    """Analyzes all Python files in the 'cli_games' folder for both models and prints comparison."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    chatgpt_dir = os.path.join(parent_dir, "results", "ChatGPT", "classEval")
    gemini_dir = os.path.join(parent_dir, "results", "Gemini", "classEval")

    try:
        chatgpt_files = sorted([f for f in os.listdir(chatgpt_dir) if f.endswith(".py")])
        gemini_files = sorted([f for f in os.listdir(gemini_dir) if f.endswith(".py")])
    except FileNotFoundError:
        print("One or both model directories not found.")
        return

    def numerical_sort_key(filename):
        match = re.search(r'code_(\d+)\.py', filename)
        if match:
            return int(match.group(1))
        return filename  

    chatgpt_files.sort(key=numerical_sort_key)
    gemini_files.sort(key=numerical_sort_key)   
    all_files = sorted(list(set(chatgpt_files + gemini_files)), key=numerical_sort_key)

    print("\n", "-" * 80)
    print("{:<20} {:<30} {:<30}".format("File", "ChatGPT LCOM", "Gemini LCOM"))
    print("-" * 80)

    for file_name in all_files:
        chatgpt_path = os.path.join(chatgpt_dir, file_name)
        gemini_path = os.path.join(gemini_dir, file_name)

        chatgpt_results = analyze_file(chatgpt_path)
        gemini_results = analyze_file(gemini_path)

        if chatgpt_results is None and gemini_results is None:
            print(f"{file_name:<20} {'File not found':<61}")
            continue

        all_classes = sorted(list(set((chatgpt_results or {}).keys()) | set((gemini_results or {}).keys())))

        for class_name in all_classes:
            chatgpt_lcom = chatgpt_results.get(class_name, ("N/A",))[0] if chatgpt_results else "N/A"
            gemini_lcom = gemini_results.get(class_name, ("N/A",))[0] if gemini_results else "N/A"

            if all_classes.index(class_name) == 0:
                print(f"{file_name:<20} {f'{class_name}: {chatgpt_lcom}':<30} {f'{class_name}: {gemini_lcom}':<30}")
            else:
                print(f"{'':<20} {f'{class_name}: {chatgpt_lcom}':<30} {f'{class_name}: {gemini_lcom}':<30}")
           
if __name__ == "__main__":
    main()
