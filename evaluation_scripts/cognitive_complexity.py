from complexipy import file_complexity
import sys
import os
import re
import statistics

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

folder_paths_gemini_cli_games = {
    "Gemini cli_games Zero-shot": os.path.join(upper_dir, "results", "Gemini", "cli_games", "Zero-shot"),
    "Gemini cli_games Zero-shot-CoT": os.path.join(upper_dir, "results", "Gemini", "cli_games", "Zero-shot-CoT"),
    "Gemini cli_games Expert-role": os.path.join(upper_dir, "results", "Gemini", "cli_games", "Expert-role"),
    "Gemini cli_games Student-role": os.path.join(upper_dir, "results", "Gemini", "cli_games", "Student-role"),
}

folder_paths_chatgpt_cli_games = {
    "ChatGPT cli_games Zero-shot": os.path.join(upper_dir, "results", "ChatGPT", "cli_games", "Zero-shot"),
    "ChatGPT cli_games Zero-shot-CoT": os.path.join(upper_dir, "results", "ChatGPT", "cli_games", "Zero-shot-CoT"),
    "ChatGPT cli_games Expert-role": os.path.join(upper_dir, "results", "ChatGPT", "cli_games", "Expert-role"),
    "ChatGPT cli_games Student-role": os.path.join(upper_dir, "results", "ChatGPT", "cli_games", "Student-role"),
}

folder_paths_gemini_classEval = {
    "Gemini classEval Zero-shot": os.path.join(upper_dir, "results", "Gemini", "classEval", "Zero-shot"),
    "Gemini classEval Zero-shot-CoT": os.path.join(upper_dir, "results", "Gemini", "classEval", "Zero-shot-CoT"),
    "Gemini classEval Expert-role": os.path.join(upper_dir, "results", "Gemini", "classEval", "Expert-role"),
    "Gemini classEval Student-role": os.path.join(upper_dir, "results", "Gemini", "classEval", "Student-role"),
}

folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir, "results", "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, "results", "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, "results", "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, "results", "ChatGPT", "classEval", "Student-role"),
}

folder_paths_chatgpt_APPS = {
    "ChatGPT APPS Zero-shot": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Zero-shot"),
    "ChatGPT APPS Zero-shot-CoT": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Zero-shot-CoT"),
    "ChatGPT APPS Expert-role": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Expert-role"),
    "ChatGPT APPS Student-role": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Student-role"),
}

folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, "results", "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, "results", "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, "results", "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, "results", "Gemini", "APPS", "Student-role"),
}

results = {}  # Store average and std dev for each folder

def analyze_folders(folder_paths, results):
    for folder_name, folder_path in folder_paths.items():
        if not os.path.exists(folder_path):
            print(f"Error: Folder not found: {folder_path}")
            continue

        if not os.path.isdir(folder_path):
            print(f"Error: Path is not a directory: {folder_path}")
            continue

        complexities = []
        all_file_names = []

        for filename in os.listdir(folder_path):
            if filename.endswith(".py"):
                all_file_names.append(filename)

        all_file_names = sorted(all_file_names, key=numerical_sort_key)

        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            try:
                fc = file_complexity(file_path)
                complexities.append(fc.complexity)
            except Exception as e:
                print(f"    Error analyzing {filename}: {e}")
                continue

        if complexities:
            average_complexity = round(statistics.mean(complexities), 2)
            std_dev_complexity = round(statistics.stdev(complexities), 2)
            results[folder_name] = (average_complexity, std_dev_complexity)
        else:
            results[folder_name] = ("No valid files", "N/A")

analyze_folders(folder_paths_gemini_cli_games, results)
analyze_folders(folder_paths_chatgpt_cli_games, results)
analyze_folders(folder_paths_gemini_classEval, results)
analyze_folders(folder_paths_chatgpt_classEval, results)
analyze_folders(folder_paths_chatgpt_APPS, results)
analyze_folders(folder_paths_gemini_APPS, results)

print("\nAverage Cognitive Complexity and Std. dev. per prompt technique:")
for folder, (avg_complexity, std_dev) in results.items():
    print(f"    {folder}: Average = {avg_complexity}, Std Dev = {std_dev}")