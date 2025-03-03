import ast
import os
import sys
import statistics

def calculate_tcc(file_path):
    """Calculates the Tight Class Cohesion (TCC) for a Python class."""

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except SyntaxError:
        print(f"Error: Syntax error in '{file_path}'.")
        return None

    class_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

    if not class_nodes:
        return None  # No classes found in the file

    class_node = class_nodes[0]  # Assuming only one class per file for simplicity

    method_names = [node.name for node in class_node.body if isinstance(node, ast.FunctionDef)]

    if len(method_names) < 2:
        return 1.0 if len(method_names) == 1 else 0.0 # TCC is 1.0 if there is only one method, and 0.0 if there are none.

    shared_variables = {}
    for method_name in method_names:
        shared_variables[method_name] = set()

    for method_node in class_node.body:
        if isinstance(method_node, ast.FunctionDef):
            method_name = method_node.name
            for node in ast.walk(method_node):
                if isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Load, ast.Store)):
                    shared_variables[method_name].add(node.id)

    connected_pairs = 0
    possible_pairs = 0

    for i in range(len(method_names)):
        for j in range(i + 1, len(method_names)):
            method1 = method_names[i]
            method2 = method_names[j]
            possible_pairs += 1
            if shared_variables[method1].intersection(shared_variables[method2]):
                connected_pairs += 1

    return connected_pairs / possible_pairs if possible_pairs > 0 else 0.0

def process_files(directory):
    """Processes all Python files in a directory and calculates their TCC."""

    results = {}
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            tcc = calculate_tcc(file_path)
            if tcc is not None:
                results[filename] = tcc
                print(f"TCC of '{filename}': {tcc}")
    return results

def calculate_statistics(results):
    """Calculates statistical data from the TCC results."""

    if not results:
        return None

    tccs = list(results.values())
    return {
        "Number of files": len(tccs),
        "Minimum TCC": min(tccs),
        "Maximum TCC": max(tccs),
        "Average TCC": statistics.mean(tccs),
        "Standard deviation": statistics.stdev(tccs) if len(tccs) > 1 else "N/A"
    }

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    chatgpt_dir = os.path.join(parent_dir, "results", "ChatGPT", "cli_games")
    gemini_dir = os.path.join(parent_dir, "results", "Gemini", "cli_games")

    chatgpt_stats = calculate_statistics(process_files(chatgpt_dir))
    gemini_stats = calculate_statistics(process_files(gemini_dir))

    print("\n--- Statistical Comparison (TCC) ---")
    print("{:<25} | {:<25}".format("ChatGPT", "Gemini"))
    print("-" * 55)

    if chatgpt_stats is None:
        print("{:<25} | {:<25}".format("No data available", "No data available"))
    else:
        for stat in chatgpt_stats:
            print("{:<25} | {:<25}".format(f"{stat}: {chatgpt_stats[stat]}", f"{stat}: {gemini_stats[stat]}"))