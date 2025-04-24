import os
import re
import statistics
import subprocess

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

def run_pylint(file_path):
    """Runs pylint on a Python file and captures the output."""
    try:
        result = subprocess.run(['pylint', '--output-format=text', file_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stdout
    except FileNotFoundError:
        return f"Error: File not found: {file_path}"
    except Exception as e:
        return f"Error running pylint on {file_path}: {e}"

def count_code_smells(pylint_output):
    """Counts the number of Pylint messages that often indicate code smells."""


    smell_indicators = [
    re.compile(r"F0002"),
    re.compile(r"F0011"),
    re.compile(r"F0001"),
    re.compile(r"F0202"),
    re.compile(r"F0010"),
    re.compile(r"F0401"),
    re.compile(r"E0110"),
    re.compile(r"E0203"),
    re.compile(r"E0237"),
    re.compile(r"E1111"),
    re.compile(r"E1128"),
    re.compile(r"E1142"),
    re.compile(r"E0014"),
    re.compile(r"E0701"),
    re.compile(r"E0705"),
    re.compile(r"E1300"),
    re.compile(r"E0013"),
    re.compile(r"E0111"),
    re.compile(r"E1310"),
    re.compile(r"E1307"),
    re.compile(r"E1003"),
    re.compile(r"E2502"),
    re.compile(r"E6005"),
    re.compile(r"E6004"),
    re.compile(r"E0712"),
    re.compile(r"E0242"),
    re.compile(r"E0116"),
    re.compile(r"E0245"),
    re.compile(r"E1141"),
    re.compile(r"E0108"),
    re.compile(r"E0241"),
    re.compile(r"E1303"),
    re.compile(r"E0102"),
    re.compile(r"E0401"),
    re.compile(r"E0240"),
    re.compile(r"E0239"),
    re.compile(r"E0100"),
    re.compile(r"E0605"),
    re.compile(r"E0604"),
    re.compile(r"E0304"),
    re.compile(r"E0308"),
    re.compile(r"E2510"),
    re.compile(r"E2511"),
    re.compile(r"E2513"),
    re.compile(r"E2514"),
    re.compile(r"E2512"),
    re.compile(r"E2515"),
    re.compile(r"E0243"),
    re.compile(r"E0244"),
    re.compile(r"E1507"),
    re.compile(r"E3701"),
    re.compile(r"E0311"),
    re.compile(r"E0313"),
    re.compile(r"E0312"),
    re.compile(r"E0309"),
    re.compile(r"E0305"),
    re.compile(r"E0310"),
    re.compile(r"E0303"),
    re.compile(r"E1139"),
    re.compile(r"E0306"),
    re.compile(r"E1126"),
    re.compile(r"E1127"),
    re.compile(r"E1144"),
    re.compile(r"E0238"),
    re.compile(r"E0236"),
    re.compile(r"E0113"),
    re.compile(r"E0307"),
    re.compile(r"E1130"),
    re.compile(r"E2501"),
    re.compile(r"E1201"),
    re.compile(r"E1206"),
    re.compile(r"E1205"),
    re.compile(r"E1200"),
    re.compile(r"E0202"),
    re.compile(r"E0704"),
    re.compile(r"E0119"),
    re.compile(r"E1304"),
    re.compile(r"E1125"),
    re.compile(r"E1302"),
    re.compile(r"E4702"),
    re.compile(r"E4703"),
    re.compile(r"E1101"),
    re.compile(r"E0211"),
    re.compile(r"E0611"),
    re.compile(r"E0213"),
    re.compile(r"E1120"),
    re.compile(r"E0301"),
    re.compile(r"E0107"),
    re.compile(r"E0115"),
    re.compile(r"E0117"),
    re.compile(r"E1134"),
    re.compile(r"E1133"),
    re.compile(r"E1701"),
    re.compile(r"E1102"),
    re.compile(r"E1129"),
    re.compile(r"E0103"),
    re.compile(r"E0711"),
    re.compile(r"E3102"),
    re.compile(r"E0606"),
    re.compile(r"E0643"),
    re.compile(r"E0702"),
    re.compile(r"E0710"),
    re.compile(r"E1124"),
    re.compile(r"E0402"),
    re.compile(r"E1132"),
    re.compile(r"E0106"),
    re.compile(r"E0101"),
    re.compile(r"E0104"),
    re.compile(r"E1519"),
    re.compile(r"E1520"),
    re.compile(r"E0114"),
    re.compile(r"E0001"),
    re.compile(r"E1306"),
    re.compile(r"E1305"),
    re.compile(r"E1121"),
    re.compile(r"E0112"),
    re.compile(r"E1301"),
    re.compile(r"E0603"),
    re.compile(r"E0602"),
    re.compile(r"E1123"),
    re.compile(r"E0302"),
    re.compile(r"E1143"),
    re.compile(r"E0633"),
    re.compile(r"E0011"),
    re.compile(r"E0015"),
    re.compile(r"E1136"),
    re.compile(r"E1137"),
    re.compile(r"E1131"),
    re.compile(r"E1138"),
    re.compile(r"E1135"),
    re.compile(r"E0601"),
    re.compile(r"E0118"),
    re.compile(r"E1700"),
    re.compile(r"E0105"),
    re.compile(r"E0235"),
    re.compile(r"E0703"),
    re.compile(r"E0012"),
    re.compile(r"E1103"),
    re.compile(r"E0234"),
    re.compile(r"E0632"),
    re.compile(r"E1140"),
]



#     smell_indicators = [
#     re.compile(r"R1260"),
#     re.compile(r"R0912"),
#     re.compile(r"R0915"),
#     re.compile(r"R1702"),
#     re.compile(r"C0103"),
#     re.compile(r"C0301"),
#     re.compile(r"W0108"),
#     re.compile(r"C0116"),
#     re.compile(r"C0115"),
#     # Potentially related to over-abstraction (less direct)
#     re.compile(r"R0903"),
#     # Basic consistency (minor initial concern)
#     re.compile(r"W1405"),
#     re.compile(r"C0327"),
#     re.compile(r"C0303"),
# ]
    count = 0
    if isinstance(pylint_output, str):
        for line in pylint_output.splitlines():
            for indicator in smell_indicators:
                if indicator.search(line):
                    count += 1
                    break  # Only count each smell once per line
    return count

def analyze_folders_and_count_code_smells(folder_paths):
    """Analyzes folders and counts potential code smells in Python files using Pylint."""
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

        smell_counts = []
        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            pylint_output = run_pylint(file_path)
            if isinstance(pylint_output, str) and not pylint_output.startswith("Error"):
                smell_count = count_code_smells(pylint_output)
                smell_counts.append(smell_count)
            else:
                print(f"Error analyzing {filename}: {pylint_output}")

        if smell_counts:
            avg_smells = smell_count
            #avg_smells = statistics.mean(smell_counts)
            std_dev_smells = statistics.stdev(smell_counts) if len(smell_counts) > 1 else 0
            results[folder_name] = (avg_smells, std_dev_smells)
        else:
            results[folder_name] = (0, 0)

    return results

# Define folder paths (same as your original script)
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Adjust if running locally.

result_setting = "results" # "filtered_results"
result_setting = "filtered_results" # "results"

# ClassEval
folder_paths_gemini_classEval = {
    "Gemini classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot"),
    "Gemini classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot-CoT"),
    "Gemini classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Expert-role"),
    "Gemini classEval Student-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
    "Gemini classEval Naive": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Naive"),
    "Gemini classEval Iterative": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Iterative"),
    "Gemini classEval Combined": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Combined"),
}

folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Naive": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Naive'),
    "ChatGPT classEval Iterative": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Iterative'),
    "ChatGPT classEval Combined": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Combined'),
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
    "ChatGPT APPS Iterative": os.path.join(upper_dir,result_setting, 'ChatGPT', 'APPS', 'Iterative'),
    "ChatGPT APPS Combined": os.path.join(upper_dir,result_setting, 'ChatGPT', 'APPS', 'Combined'),
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

folder_paths_ground_truth_classEval = {
        "GroundTruth classEval": os.path.join(upper_dir, "ground_truth", "classEval")
    }
folder_paths_ground_truth_APPS = {
        "GroundTruth APPS": os.path.join(upper_dir, "ground_truth", "APPS")
    }

# Analyze folders and count code smells
results_gemini = {}
results_chatgpt = {}
results_gemma = {}
ground_truth = {}

results_chatgpt.update(analyze_folders_and_count_code_smells(folder_paths_chatgpt_classEval))
results_gemini.update(analyze_folders_and_count_code_smells(folder_paths_gemini_classEval))
results_gemma.update(analyze_folders_and_count_code_smells(folder_paths_gemma_classEval))
ground_truth.update(analyze_folders_and_count_code_smells(folder_paths_ground_truth_classEval))

results_chatgpt.update(analyze_folders_and_count_code_smells(folder_paths_chatgpt_APPS))
results_gemini.update(analyze_folders_and_count_code_smells(folder_paths_gemini_APPS))
results_gemma.update(analyze_folders_and_count_code_smells(folder_paths_gemma_APPS))
ground_truth.update(analyze_folders_and_count_code_smells(folder_paths_ground_truth_APPS))

print("\nAverage Code Smell Count per Folder (based on selected Pylint messages):")
for folder, (avg_smells, std_dev_smells) in results_gemini.items():
    print(f"  Gemini {folder}: Average Smells = {avg_smells:.2f}")

for folder, (avg_smells, std_dev_smells) in results_chatgpt.items():
    print(f"  ChatGPT {folder}: Average Smells = {avg_smells:.2f}")

for folder, (avg_smells, std_dev_smells) in results_gemma.items():
    print(f"  Gemma3 {folder}: Average Smells = {avg_smells:.2f}")

for folder, (avg_smells, std_dev_smells) in ground_truth.items():
    print(f"  {folder}: Average Smells = {avg_smells:.2f}")

# Split smell count by technique for Gemini
gemini_smell_counts = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Naive": [],
    "Iterative": [],
    "Combined": [],
}

# Split smell count by technique for ChatGPT
chatgpt_smell_counts = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Naive": [],
    "Iterative": [],
    "Combined": [],
}

# Split smell count by technique for Gemma3
gemma_smell_counts = {
    "Zero-shot": [],
    "Zero-shot-CoT": [],
    "Expert-role": [],
    "Student-role": [],
    "Naive": [],
    "Iterative": [],
    "Combined": [],
}

for folder, (avg_smells, _) in results_gemini.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        gemini_smell_counts["Zero-shot"].append(avg_smells)
    elif "Zero-shot-CoT" in folder:
        gemini_smell_counts["Zero-shot-CoT"].append(avg_smells)
    elif "Expert-role" in folder:
        gemini_smell_counts["Expert-role"].append(avg_smells)
    elif "Student-role" in folder:
        gemini_smell_counts["Student-role"].append(avg_smells)
    elif "Naive" in folder:
        gemini_smell_counts["Naive"].append(avg_smells)
    elif "Iterative" in folder:
        gemini_smell_counts["Iterative"].append(avg_smells)
    elif "Combined" in folder:
        gemini_smell_counts["Combined"].append(avg_smells)

for folder, (avg_smells, _) in results_chatgpt.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_smell_counts["Zero-shot"].append(avg_smells)
    elif "Zero-shot-CoT" in folder:
        chatgpt_smell_counts["Zero-shot-CoT"].append(avg_smells)
    elif "Expert-role" in folder:
        chatgpt_smell_counts["Expert-role"].append(avg_smells)
    elif "Student-role" in folder:
        chatgpt_smell_counts["Student-role"].append(avg_smells)
    elif "Naive" in folder:
        chatgpt_smell_counts["Naive"].append(avg_smells)
    elif "Iterative" in folder:
        chatgpt_smell_counts["Iterative"].append(avg_smells)
    elif "Combined" in folder:
        chatgpt_smell_counts["Combined"].append(avg_smells)

for folder, (avg_smells, _) in results_gemma.items(): #ignore standard deviation from folder output
    if "Zero-shot" in folder and "CoT" not in folder:
        gemma_smell_counts["Zero-shot"].append(avg_smells)
    elif "Zero-shot-CoT" in folder:
        gemma_smell_counts["Zero-shot-CoT"].append(avg_smells)
    elif "Expert-role" in folder:
        gemma_smell_counts["Expert-role"].append(avg_smells)
    elif "Student-role" in folder:
        gemma_smell_counts["Student-role"].append(avg_smells)
    elif "Naive" in folder:
        gemma_smell_counts["Naive"].append(avg_smells)
    elif "Iterative" in folder:
        gemma_smell_counts["Iterative"].append(avg_smells)
    elif "Combined" in folder:
        gemma_smell_counts["Combined"].append(avg_smells)

print("\nGemini Average Code Smell Counts:")
for technique, counts in gemini_smell_counts.items():
    if counts:
        avg_count = statistics.mean(counts)
        std_dev_count = statistics.stdev(counts) if len(counts) > 1 else 0
        print(f"  {technique}: Average Smells = {avg_count:.2f}")
    else:
        print(f"  {technique}: No data available.")

print("\nChatGPT Average Code Smell Counts:")
for technique, counts in chatgpt_smell_counts.items():
    if counts:
        avg_count = statistics.mean(counts)
        std_dev_count = statistics.stdev(counts) if len(counts) > 1 else 0
        print(f"  {technique}: Average Smells = {avg_count:.2f}")
    else:
        print(f"  {technique}: No data available.")

print("\nGemma3 Average Code Smell Counts:")
for technique, counts in gemma_smell_counts.items():
    if counts:
        avg_count = statistics.mean(counts)
        std_dev_count = statistics.stdev(counts) if len(counts) > 1 else 0
        print(f"  {technique}: Average Smells = {avg_count:.2f}")
    else:
        print(f"  {technique}: No data available.")