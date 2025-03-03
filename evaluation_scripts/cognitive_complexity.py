import ast
import os
import sys
import statistics

def calculate_cognitive_complexity(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except SyntaxError:
        print(f"Error: Syntax error in '{file_path}'.")
        return None

    complexity = 0
    nesting_level = 0

    def visit(node):
        nonlocal complexity, nesting_level

        if isinstance(node, (ast.If, ast.While, ast.For, ast.Try, ast.ExceptHandler)):
            complexity += 1 + nesting_level
            nesting_level += 1

        elif isinstance(node, (ast.BoolOp, ast.Compare)):
            complexity += len(getattr(node, 'ops', []))

        elif isinstance(node, ast.Break):
            complexity += 1

        elif isinstance(node, ast.FunctionDef):
            nesting_level = 0

        for child in ast.iter_child_nodes(node):
            visit(child)

        if isinstance(node, (ast.If, ast.While, ast.For, ast.Try, ast.ExceptHandler)):
            nesting_level -= 1

    visit(tree)
    return complexity

def process_files(directory, complexity_function):  # Added complexity_function argument
    """
    Processes all Python files in a directory and calculates their complexity.

    Args:
        directory (str): The directory containing Python files.
        complexity_function (function): The complexity calculation function.
    """
    results = {}
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            complexity = complexity_function(file_path)  # Use the passed function
            if complexity is not None:
                results[filename] = complexity
    return results

def calculate_statistics(results):
    """
    Calculates statistical data from the complexity results.

    Args:
        results (dict): A dictionary containing filename:complexity pairs.
    """
    if not results:
        return None  # Return None if no results

    complexities = list(results.values())
    return {
        "Number of files": len(complexities),
        "Minimum complexity": min(complexities),
        "Maximum complexity": max(complexities),
        "Average complexity": statistics.mean(complexities),
        "Standard deviation": statistics.stdev(complexities) if len(complexities) > 1 else "N/A"
    }

if __name__ == "__main__":
    # Get the parent directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # Construct the path to the desired directory
    chatgpt_dir = os.path.join(parent_dir, "results", "ChatGPT", "cli_games")
    gemini_dir = os.path.join(parent_dir, "results", "Gemini", "cli_games")

    chatgpt_stats = calculate_statistics(process_files(chatgpt_dir))
    gemini_stats = calculate_statistics(process_files(gemini_dir))

    print("\n--- Statistical Comparison ---")
    print("{:<25} | {:<25}".format("ChatGPT", "Gemini"))
    print("-" * 55)  # Separator line

    if chatgpt_stats is None:
        print("{:<25} | {:<25}".format("No data available", "No data available"))
    else:
        for stat in chatgpt_stats:
            print("{:<25} | {:<25}".format(f"{stat}: {chatgpt_stats[stat]}", f"{stat}: {gemini_stats[stat]}"))