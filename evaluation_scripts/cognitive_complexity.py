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
#result_setting = "results" # "filtered_results"


# ClassEval

# ClassEval
folder_paths_ground_truth_classEval = {
    "GroundTruth classEval": os.path.join(upper_dir, "ground_truth", "classEval")
}

folder_paths_ground_truth_APPS = {
    "GroundTruth APPS": os.path.join(upper_dir, "ground_truth", "APPS")
}




folder_paths_gemini_classEval = {
    "Gemini classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot"),
    "Gemini classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot-CoT"),
    "Gemini classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Expert-role"),
    "Gemini classEval Student-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
    "Gemini classEval Naive": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
    "Gemini classEval Iterative": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Iterative"),
    "Gemini classEval Combined": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Combined"),
}
folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir,result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Naive": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Naive"),
    "ChatGPT classEval Iterative": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Iterative"),
    "ChatGPT classEval Combined": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Combined"),
}
folder_paths_gemma_classEval = {
    "Gemma3 classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot"),
    "Gemma3 classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot-CoT"),
    "Gemma3 classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Expert-role"),
    "Gemma3 classEval Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Student-role"),
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
    "ChatGPT APPS Naive": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Naive"),
    "ChatGPT APPS Iterative": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Iterative"),
    "ChatGPT APPS Combined": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Combined"),
}
folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Student-role"),
    "Gemini APPS Naive": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Naive"),
    "Gemini APPS Iterative": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Iterative"),
    "Gemini APPS Combined": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Combined"),
}
folder_paths_gemma_APPS = {
    "Gemma3 APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot"),
    "Gemma3 APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot-CoT"),
    "Gemma3 APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Expert-role"),
    "Gemma3 APPS Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Student-role"),
    "Gemma3 APPS Naive": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Naive"),
    "Gemma3 APPS Iterative": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Iterative"),
    "Gemma3 APPS Combined": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Combined"),
}




results_chatgpt = {}  # Store category counts for each folder
results_gemini = {}
results_gemma = {}
ground_truth ={}


def get_complexity_category(complexity_value):
    """Categorizes cognitive complexity into four classes."""
    if complexity_value < 5:
        return "low"
    elif 6 <= complexity_value <= 10:
        return "moderate"
    elif 11 <= complexity_value <= 20:
        return "high"
    elif complexity_value >= 21:
        return "very high"
    return "N/A"

def analyze_folders(folder_paths, results):
    for folder_name, folder_path in folder_paths.items():

        if not os.path.exists(folder_path):
            print(f"Error: Folder not found: {folder_path}")
            continue

        if not os.path.isdir(folder_path):
            print(f"Error: Path is not a directory: {folder_path}")
            continue

        category_counts = {"low": 0, "moderate": 0, "high": 0, "very high": 0}
        all_file_names = []

        for filename in os.listdir(folder_path):
            if filename.endswith(".py"):
                all_file_names.append(filename)

        all_file_names = sorted(all_file_names, key=numerical_sort_key)

        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            try:
                fc = file_complexity(file_path)
                category = get_complexity_category(fc.complexity)
                category_counts[category] += 1
            except Exception as e:
                print(f"  Error analyzing {filename}: {e}")
                continue

        results[folder_name] = category_counts

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

# Ground truth
# analyze_folders(folder_paths_ground_truth_APPS, ground_truth)
# analyze_folders(folder_paths_ground_truth_classEval, ground_truth)



print("\nCognitive Complexity Category Distribution per prompt technique:")

for folder, counts in results_gemini.items():
    print(f"  {folder}: Low = {counts['low']}, Moderate = {counts['moderate']}, High = {counts['high']}, Very High = {counts['very high']}")

for folder, counts in results_chatgpt.items():
    print(f"  {folder}: Low = {counts['low']}, Moderate = {counts['moderate']}, High = {counts['high']}, Very High = {counts['very high']}")

for folder, counts in results_gemma.items():
    print(f"  {folder}: Low = {counts['low']}, Moderate = {counts['moderate']}, High = {counts['high']}, Very High = {counts['very high']}")

for folder, counts in ground_truth.items():
    print(f"  {folder}: Low = {counts['low']}, Moderate = {counts['moderate']}, High = {counts['high']}, Very High = {counts['very high']}")