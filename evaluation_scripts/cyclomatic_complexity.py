import ast
import os
import sys
import statistics

def calculate_cyclomatic_complexity(file_path):
    """
    Calculates the cyclomatic complexity of a Python file.

    Args:
        file_path (str): The path to the Python file.

    Returns:
        int: The cyclomatic complexity score, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except SyntaxError:
        print(f"Error: Syntax error in '{file_path}'.")
        return None

    complexity = 1  # Base complexity

    def visit(node):
        nonlocal complexity

        if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.With, ast.BoolOp, ast.Try)):
            if isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1 # BoolOp contributes n-1 to the complexity
            else:
                complexity += 1
        elif isinstance(node, ast.comprehension):
            complexity += 1
        elif isinstance(node, ast.excepthandler):
            complexity +=1

        for child in ast.iter_child_nodes(node):
            visit(child)

    visit(tree)
    return complexity

def process_files(directory):
    """
    Processes all Python files in a directory and calculates their cyclomatic complexity.

    Args:
        directory (str): The directory containing Python files.
    """
    results = {}
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            complexity = calculate_cyclomatic_complexity(file_path)
            if complexity is not None:
                results[filename] = complexity
                print(f"Cyclomatic complexity of '{filename}': {complexity}")
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

    print("\n--- Statistical Comparison (Cyclomatic Complexity) ---")
    print("{:<25} | {:<25}".format("ChatGPT", "Gemini"))
    print("-" * 55)  # Separator line

    if chatgpt_stats is None:
        print("{:<25} | {:<25}".format("No data available", "No data available"))
    else:
        for stat in chatgpt_stats:
            print("{:<25} | {:<25}".format(f"{stat}: {chatgpt_stats[stat]}", f"{stat}: {gemini_stats[stat]}"))