import os
import re
import statistics
import radon.raw

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

def calculate_comment_density(file_path):
    """Calculates the comment percentage (as a decimal) of a Python file using Radon, excluding blank lines."""
    try:
        with open(file_path, 'r') as f:
            code_string = f.read()
        results = radon.raw.analyze(code_string)
        if results:
            loc = results.loc - results.blank  # Subtract blank lines from total LOC
            comments = results.comments
            if loc + comments > 0:
                return 100*comments / (loc + comments)
            else:
                return 0.0
        else:
            return 0.0
    except FileNotFoundError:
        return 0.0
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return 0.0

def analyze_folders_and_count_comment_density(folder_paths):
    """Analyzes folders and counts comment percentage (as a decimal) in Python files."""
    results = {}
    for folder_name, folder_path in folder_paths.items():
        if not os.path.exists(folder_path):
            print(f"Error: Folder not found: {folder_path}")
            continue

        if not os.path.isdir(folder_path):
            print(f"Error: Path is not a directory: {folder_path}")
            continue

        all_file_names = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".py"):
                all_file_names.append(filename)

        all_file_names = sorted(all_file_names, key=numerical_sort_key)

        percentages = []
        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            percentage = calculate_comment_density(file_path)
            if percentage is not None:
                percentages.append(percentage)
            else:
                print(f"Error analyzing {filename}")

        if percentages:
            avg_percentage = statistics.mean(percentages)
            std_dev_percentage = statistics.stdev(percentages) if len(percentages) > 1 else 0
            results[folder_name] = (avg_percentage, std_dev_percentage)
        else:
            results[folder_name] = (0, 0)

    return results


# Define folder paths (same as your original script)
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Adjust if running locally.

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
    "ChatGPT APPS Meta": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Meta"),
    "ChatGPT APPS Naive": os.path.join(upper_dir, "results", "ChatGPT", "APPS", "Naive"),
}

folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, "results", "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, "results", "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, "results", "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, "results", "Gemini", "APPS", "Student-role"),
}

# Analyze folders and count comment density
results_gemini = analyze_folders_and_count_comment_density(folder_paths_gemini_cli_games)
results_chatgpt = analyze_folders_and_count_comment_density(folder_paths_chatgpt_cli_games)
results_gemini.update(analyze_folders_and_count_comment_density(folder_paths_gemini_classEval))
results_chatgpt.update(analyze_folders_and_count_comment_density(folder_paths_chatgpt_classEval))
results_chatgpt.update(analyze_folders_and_count_comment_density(folder_paths_chatgpt_APPS))
results_gemini.update(analyze_folders_and_count_comment_density(folder_paths_gemini_APPS))

print("\nComment Density per Folder:")
for folder, (avg_density, std_dev_density) in results_gemini.items():
    print(f"  {folder}: Average Density = {avg_density:.4f}")

for folder, (avg_density, std_dev_density) in results_chatgpt.items():
    print(f"  {folder}: Average Density = {avg_density:.4f}")

# Split density calculation by technique for Gemini
gemini_densities = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
}

# Split density calculation by technique for ChatGPT
chatgpt_densities = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
}

for folder, (avg_density, _) in results_gemini.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        gemini_densities["Zero-shot"].append(avg_density)
    elif "Zero-shot-CoT" in folder:
        gemini_densities["Zero-shot-CoT"].append(avg_density)
    elif "Expert-role" in folder:
        gemini_densities["Expert-role"].append(avg_density)
    elif "Student-role" in folder:
        gemini_densities["Student-role"].append(avg_density)

for folder, (avg_density, _) in results_chatgpt.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_densities["Zero-shot"].append(avg_density)
    elif "Zero-shot-CoT" in folder:
        chatgpt_densities["Zero-shot-CoT"].append(avg_density)
    elif "Expert-role" in folder:
        chatgpt_densities["Expert-role"].append(avg_density)
    elif "Student-role" in folder:
        chatgpt_densities["Student-role"].append(avg_density)

print("\nGemini Comment Density Averages:")
for technique, densities in gemini_densities.items():
    if densities:
        avg_density = statistics.mean(densities)
        std_dev_density = statistics.stdev(densities) if len(densities) > 1 else 0
        print(f"  {technique}: Average Density = {avg_density:.4f}")
    else:
        print(f"  {technique}: No data available.")

print("\nChatGPT Comment Density Averages:")
for technique, densities in chatgpt_densities.items():
    if densities:
        avg_density = statistics.mean(densities)
        std_dev_density = statistics.stdev(densities) if len(densities) > 1 else 0
        print(f"  {technique}: Average Density = {avg_density:.4f}")
    else:
        print(f"  {technique}: No data available.")