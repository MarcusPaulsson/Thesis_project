
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



result_setting = "results" # "filtered_results"
#result_setting = "filtered_results" # "results"

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
    "Gemini classEval Naive": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Naive"),
    "Gemini classEval Iterative": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Iterative"),
    "Gemini classEval Combined": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Combined"),
}

folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Meta": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Meta'),
    "ChatGPT classEval Naive": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Naive'),
    "ChatGPT classEval Iterative": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Iterative'),
    "ChatGPT classEval Combined": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Combined'),
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
    "ChatGPT APPS Iterative": os.path.join(upper_dir,result_setting, 'ChatGPT', 'APPS', 'Iterative'),
    "ChatGPT APPS Combined": os.path.join(upper_dir,result_setting, 'ChatGPT', 'APPS', 'Combined'),
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

# Analyze folders and count comment density
# results_gemini = analyze_folders_and_count_comment_density(folder_paths_gemini_cli_games)
# results_chatgpt = analyze_folders_and_count_comment_density(folder_paths_chatgpt_cli_games)

results_gemini={}  
results_chatgpt ={} 
results_gemma ={} 

results_chatgpt.update(analyze_folders_and_count_comment_density(folder_paths_chatgpt_classEval))
results_gemini.update(analyze_folders_and_count_comment_density(folder_paths_gemini_classEval))
results_gemma.update(analyze_folders_and_count_comment_density(folder_paths_gemma_classEval))

results_chatgpt.update(analyze_folders_and_count_comment_density(folder_paths_chatgpt_APPS))
results_gemini.update(analyze_folders_and_count_comment_density(folder_paths_gemini_APPS))
results_gemma.update(analyze_folders_and_count_comment_density(folder_paths_gemma_APPS))

print("\nComment Density per Folder:")
for folder, (avg_density, std_dev_density) in results_gemini.items():
    print(f"  {folder}: Average Density = {avg_density:.4f}")

for folder, (avg_density, std_dev_density) in results_chatgpt.items():
    print(f"  {folder}: Average Density = {avg_density:.4f}")

for folder, (avg_density, std_dev_density) in results_gemma.items():
    print(f"  {folder}: Average Density = {avg_density:.4f}")

# Split density calculation by technique for Gemini
gemini_densities = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Meta": [],
    "Naive": [],
    "Iterative" :[],
    "Combined" :[],
}

# Split density calculation by technique for ChatGPT
chatgpt_densities = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Meta": [],
    "Naive": [],
    "Iterative":[], 
    "Combined" :[],
}

# Split density calculation by technique for ChatGPT
gemma_densities = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Meta": [],
    "Naive": [],
    "Iterative":[], 
    "Combined" :[],
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
    elif "Meta" in folder:
        gemini_densities["Meta"].append(avg_density)
    elif "Naive" in folder:
        gemini_densities["Naive"].append(avg_density)
    elif "Iterative" in folder:
        gemini_densities["Iterative"].append(avg_density)
    elif "Combined" in folder:
        gemini_densities["Combined"].append(avg_density)


for folder, (avg_density, _) in results_chatgpt.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_densities["Zero-shot"].append(avg_density)
    elif "Zero-shot-CoT" in folder:
        chatgpt_densities["Zero-shot-CoT"].append(avg_density)
    elif "Expert-role" in folder:
        chatgpt_densities["Expert-role"].append(avg_density)
    elif "Student-role" in folder:
        chatgpt_densities["Student-role"].append(avg_density)
    elif "Meta" in folder:
        chatgpt_densities["Meta"].append(avg_density)
    elif "Naive" in folder:
        chatgpt_densities["Naive"].append(avg_density)
    elif "Iterative" in folder:
        chatgpt_densities["Iterative"].append(avg_density)
    elif "Combined" in folder:
        gemini_densities["Combined"].append(avg_density)

for folder, (avg_density, _) in results_gemma.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_densities["Zero-shot"].append(avg_density)
    elif "Zero-shot-CoT" in folder:
        chatgpt_densities["Zero-shot-CoT"].append(avg_density)
    elif "Expert-role" in folder:
        chatgpt_densities["Expert-role"].append(avg_density)
    elif "Student-role" in folder:
        chatgpt_densities["Student-role"].append(avg_density)
    elif "Meta" in folder:
        chatgpt_densities["Meta"].append(avg_density)
    elif "Naive" in folder:
        chatgpt_densities["Naive"].append(avg_density)
    elif "Iterative" in folder:
        chatgpt_densities["Iterative"].append(avg_density)
    elif "Combined" in folder:
        chatgpt_densities["Combined"].append(avg_density)

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

print("\nChatGPT Comment Density Averages:")
for technique, densities in gemma_densities.items():
    if densities:
        avg_density = statistics.mean(densities)
        std_dev_density = statistics.stdev(densities) if len(densities) > 1 else 0
        print(f"  {technique}: Average Density = {avg_density:.4f}")
    else:
        print(f"  {technique}: No data available.")