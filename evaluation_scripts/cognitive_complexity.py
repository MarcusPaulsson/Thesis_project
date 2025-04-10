from complexipy import file_complexity
import sys
import os
import re
import statistics
import math

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

# EVALUATING ALL RESULTS

result_setting = "filtered_results" # "results"
result_setting = "results" # "filtered_results"

# folder_paths_gemini_cli_games = {
#     "Gemini cli_games Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Zero-shot"),
#     "Gemini cli_games Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Zero-shot-CoT"),
#     "Gemini cli_games Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Expert-role"),
#     "Gemini cli_games Student-role": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Student-role"),
# }

# folder_paths_chatgpt_cli_games = {
#     "ChatGPT cli_games Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Zero-shot"),
#     "ChatGPT cli_games Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Zero-shot-CoT"),
#     "ChatGPT cli_games Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Expert-role"),
#     "ChatGPT cli_games Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Student-role"),
# }

# ClassEval
folder_paths_gemini_classEval = {
    "Gemini classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot"),
    "Gemini classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot-CoT"),
    "Gemini classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Expert-role"),
    "Gemini classEval Student-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
    "Gemini classEval Meta": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Meta"),
    "Gemini classEval Naive": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
    "Gemini classEval Iterative": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Iterative"),
    "Gemini classEval Combined": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Combined"),
}
folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir,result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval test": os.path.join(upper_dir,result_setting, "ChatGPT_test", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Meta": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Meta"),
    "ChatGPT classEval Naive": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Naive"),
    "ChatGPT classEval Iterative": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Iterative"),
    "ChatGPT classEval Combined": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Combined"),
}
folder_paths_gemma_classEval = {
    "Gemma3 classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot"),
    "Gemma3 classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot-CoT"),
    "Gemma3 classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Expert-role"),
    "Gemma3 classEval Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Student-role"),
    "Gemma3 classEval Meta": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Meta"),
    "Gemma3 classEval Naive": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Naive"),
    "Gemma3 classEval Iterative": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Iterative"),
    "Gemma3 classEval Combined": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Combined"),
}


# APPS
folder_paths_chatgpt_APPS = {
    "ChatGPT APPS Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Zero-shot"),
    "ChatGPT APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Zero-shot-CoT"),
    "ChatGPT APPS Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Expert-role"),
    "ChatGPT APPS Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Student-role"),
    "ChatGPT APPS Meta": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Meta"),
    "ChatGPT APPS Naive": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Naive"),
    "ChatGPT APPS Iterative": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Iterative"),
    "ChatGPT APPS Combined": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Combined"),
}
folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Student-role"),
    "Gemini APPS Meta": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Meta"),
    "Gemini APPS Naive": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Naive"),
    "Gemini APPS Iterative": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Iterative"),
    "Gemini APPS Combined": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Combined"),
}
folder_paths_gemma_APPS = {
    "Gemma3 APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot"),
    "Gemma3 APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot-CoT"),
    "Gemma3 APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Expert-role"),
    "Gemma3 APPS Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Student-role"),
    "Gemma3 APPS Meta": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Meta"),
    "Gemma3 APPS Naive": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Naive"),
    "Gemma3 APPS Iterative": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Iterative"),
    "Gemma3 APPS Combined": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Combined"),
}




results_chatgpt = {}  # Store average and std dev for each folder
results_gemini = {}
results_gemma = {}

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
                print(f"  Error analyzing {filename}: {e}")
                continue

        if complexities:
            average_complexity = round(statistics.mean(complexities), 2)
            std_dev_complexity = round(statistics.stdev(complexities), 2)
            results[folder_name] = (average_complexity, std_dev_complexity)
        else:
            results[folder_name] = ("No valid files", "N/A")

def geometric_mean(data):
    if not data:
        return "N/A"
    product = 1
    for x in data:
        product *= x
    return round(math.pow(product, 1 / len(data)), 2)

# analyze_folders(folder_paths_gemini_cli_games, results_gemini)
# analyze_folders(folder_paths_chatgpt_cli_games, results_chatgpt)

analyze_folders(folder_paths_gemini_classEval, results_gemini)
analyze_folders(folder_paths_chatgpt_classEval, results_chatgpt)
analyze_folders(folder_paths_chatgpt_APPS, results_chatgpt)
analyze_folders(folder_paths_gemini_APPS, results_gemini)
analyze_folders(folder_paths_gemma_APPS, results_gemma)
analyze_folders(folder_paths_gemma_classEval, results_gemma)

print_std_dev = False  # Changed to True to print standard deviation

print("\nAverage Cognitive Complexity per prompt technique:")

for folder, (avg_complexity, std_dev) in results_gemini.items():
    if print_std_dev:
        print(f"  {folder}: Average = {avg_complexity}, Std Dev = {std_dev}")
    else:
        print(f"  {folder}: Average = {avg_complexity}")

for folder, (avg_complexity, std_dev) in results_chatgpt.items():
    if print_std_dev:
        print(f"  {folder}: Average = {avg_complexity}, Std Dev = {std_dev}")
    else:
        print(f"  {folder}: Average = {avg_complexity}")

for folder, (avg_complexity, std_dev) in results_gemma.items():
    if print_std_dev:
        print(f"  {folder}: Average = {avg_complexity}, Std Dev = {std_dev}")
    else:
        print(f"  {folder}: Average = {avg_complexity}")
