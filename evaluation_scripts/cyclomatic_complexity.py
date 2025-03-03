import os
import statistics
import lizard

def calculate_cyclomatic_complexity(file_path):
    """
    Calculates the cyclomatic complexity of a Python file using lizard.
    """
    try:
        analysis = lizard.analyze_file(file_path)
        return sum(func.cyclomatic_complexity for func in analysis.function_list)
    except Exception:
        return None

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
    """
    if not results:
        return None
    
    complexities = list(results.values())
    return {
        "Number of files": len(complexities),
        "Minimum complexity": min(complexities),
        "Maximum complexity": max(complexities),
        "Average complexity": statistics.mean(complexities),
        "Standard deviation": statistics.stdev(complexities) if len(complexities) > 1 else "N/A"
    }

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    chatgpt_dir = os.path.join(parent_dir, "results", "ChatGPT", "cli_games")
    gemini_dir = os.path.join(parent_dir, "results", "Gemini", "cli_games")

    chatgpt_results = process_files(chatgpt_dir)
    gemini_results = process_files(gemini_dir)

    chatgpt_stats = calculate_statistics(chatgpt_results)
    gemini_stats = calculate_statistics(gemini_results)

    print("\n--- Statistical Comparison (Cyclomatic Complexity) ---")
    print("{:<25} | {:<25}".format("ChatGPT", "Gemini"))
    print("-" * 55)

    if chatgpt_stats is None or gemini_stats is None:
        print("{:<25} | {:<25}".format("No data available", "No data available"))
    else:
        for stat in chatgpt_stats:
            print("{:<25} | {:<25}".format(f"{stat}: {chatgpt_stats[stat]}", f"{stat}: {gemini_stats[stat]}"))

    print("\n--- File-wise Comparison ---")
    print("{:<30} {:<10}".format("File", "Lizard"))
    print("-" * 60)

    for filename, complexity in chatgpt_results.items():
        print("{:<30} {:<10}".format(filename, complexity))
