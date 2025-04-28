import os
import re
import statistics
import radon.raw
import radon.metrics  # For maintainability index

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

def calculate_metrics(file_path):
    """Calculates both LOC and Maintainability Index of a Python file using Radon."""
    try:
        with open(file_path, 'r') as f:
            code_string = f.read()
        raw_results = radon.raw.analyze(code_string)
        mi_score = radon.metrics.mi_visit(code_string, multi=True)
        
        return {
            'loc': raw_results.loc if raw_results else 0,  # Total lines of code including comments and blank lines
            'mi': mi_score  # Maintainability Index
        }
    except FileNotFoundError:
        return {'loc': 0, 'mi': 0}
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return {'loc': 0, 'mi': 0}

def analyze_folders_and_count_metrics(folder_paths):
    """Analyzes folders and counts Lines of Code and Maintainability Index in Python files."""
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

        loc_values = []
        mi_values = []
        
        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            metrics = calculate_metrics(file_path)
            loc_values.append(metrics['loc'])
            mi_values.append(metrics['mi'])

        if loc_values:
            # LOC statistics
            avg_loc = statistics.mean(loc_values)
            median_loc = statistics.median(loc_values)
            min_loc = min(loc_values)
            max_loc = max(loc_values)
            std_dev_loc = statistics.stdev(loc_values) if len(loc_values) > 1 else 0
            total_loc = sum(loc_values)
            
            # MI statistics
            avg_mi = statistics.mean(mi_values)
            median_mi = statistics.median(mi_values)
            min_mi = min(mi_values)
            max_mi = max(mi_values)
            std_dev_mi = statistics.stdev(mi_values) if len(mi_values) > 1 else 0
            
            file_count = len(loc_values)
            
            results[folder_name] = {
                'average_loc': avg_loc,
                'median_loc': median_loc,
                'min_loc': min_loc,
                'max_loc': max_loc,
                'std_dev_loc': std_dev_loc,
                'total_loc': total_loc,
                'average_mi': avg_mi,
                'median_mi': median_mi,
                'min_mi': min_mi,
                'max_mi': max_mi,
                'std_dev_mi': std_dev_mi,
                'file_count': file_count
            }
        else:
            results[folder_name] = {
                'average_loc': 0,
                'median_loc': 0,
                'min_loc': 0,
                'max_loc': 0,
                'std_dev_loc': 0,
                'total_loc': 0,
                'average_mi': 0,
                'median_mi': 0,
                'min_mi': 0,
                'max_mi': 0,
                'std_dev_mi': 0,
                'file_count': 0
            }

    return results


# Define folder paths (same as your original script)
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Adjust if running locally.

filtered = True
if filtered: result_setting="filtered_results"
else: result_setting = "results" 

if filtered: ground_truth = "ground_truth_filtered"
else: ground_truth = "ground_truth"

# ClassEval
folder_paths_ground_truth_classEval = {
    "GroundTruth classEval": os.path.join(upper_dir, ground_truth, "classEval")
}

folder_paths_ground_truth_APPS = {
    "GroundTruth APPS": os.path.join(upper_dir, ground_truth, "APPS")
}

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


# Analyze folders and count LOC and MI
results_gemini = {}
results_chatgpt = {}
results_gemma = {}
ground_truth ={}

results_chatgpt.update(analyze_folders_and_count_metrics(folder_paths_chatgpt_classEval))
results_gemini.update(analyze_folders_and_count_metrics(folder_paths_gemini_classEval))
results_gemma.update(analyze_folders_and_count_metrics(folder_paths_gemma_classEval))


results_chatgpt.update(analyze_folders_and_count_metrics(folder_paths_chatgpt_APPS))
results_gemini.update(analyze_folders_and_count_metrics(folder_paths_gemini_APPS))
results_gemma.update(analyze_folders_and_count_metrics(folder_paths_gemma_APPS))

# Ground truth
ground_truth.update(analyze_folders_and_count_metrics(folder_paths_ground_truth_APPS))
ground_truth.update(analyze_folders_and_count_metrics(folder_paths_ground_truth_classEval))



print("\nMetrics Statistics per Folder:")
for folder, stats in results_gemini.items():
    print(f"{folder}:")
    print(f"  Average LOC: {stats['average_loc']:.2f}")
    print(f"  Median LOC: {stats['median_loc']:.2f}")
    print(f"  Min LOC: {stats['min_loc']}")
    print(f"  Max LOC: {stats['max_loc']}")
    print(f"  Total LOC: {stats['total_loc']}")
    print(f"  Average MI: {stats['average_mi']:.2f}")
    print(f"  Median MI: {stats['median_mi']:.2f}")
    print(f"  Min MI: {stats['min_mi']:.2f}")
    print(f"  Max MI: {stats['max_mi']:.2f}")
    print(f"  File Count: {stats['file_count']}")

for folder, stats in results_chatgpt.items():
    print(f"{folder}:")
    print(f"  Average LOC: {stats['average_loc']:.2f}")
    print(f"  Median LOC: {stats['median_loc']:.2f}")
    print(f"  Min LOC: {stats['min_loc']}")
    print(f"  Max LOC: {stats['max_loc']}")
    print(f"  Total LOC: {stats['total_loc']}")
    print(f"  Average MI: {stats['average_mi']:.2f}")
    print(f"  Median MI: {stats['median_mi']:.2f}")
    print(f"  Min MI: {stats['min_mi']:.2f}")
    print(f"  Max MI: {stats['max_mi']:.2f}")
    print(f"  File Count: {stats['file_count']}")

for folder, stats in results_gemma.items():
    print(f"{folder}:")
    print(f"  Average LOC: {stats['average_loc']:.2f}")
    print(f"  Median LOC: {stats['median_loc']:.2f}")
    print(f"  Min LOC: {stats['min_loc']}")
    print(f"  Max LOC: {stats['max_loc']}")
    print(f"  Total LOC: {stats['total_loc']}")
    print(f"  Average MI: {stats['average_mi']:.2f}")
    print(f"  Median MI: {stats['median_mi']:.2f}")
    print(f"  Min MI: {stats['min_mi']:.2f}")
    print(f"  Max MI: {stats['max_mi']:.2f}")
    print(f"  File Count: {stats['file_count']}")

for folder, stats in ground_truth.items():
    print(f"{folder}:")
    print(f"  Average LOC: {stats['average_loc']:.2f}")
    print(f"  Median LOC: {stats['median_loc']:.2f}")
    print(f"  Min LOC: {stats['min_loc']}")
    print(f"  Max LOC: {stats['max_loc']}")
    print(f"  Total LOC: {stats['total_loc']}")
    print(f"  Average MI: {stats['average_mi']:.2f}")
    print(f"  Median MI: {stats['median_mi']:.2f}")
    print(f"  Min MI: {stats['min_mi']:.2f}")
    print(f"  Max MI: {stats['max_mi']:.2f}")
    print(f"  File Count: {stats['file_count']}")


# Split MI calculation by technique for all models
gemini_metrics = {
    "Zero-shot": {"loc": [], "mi": []},
    "Zero-shot-CoT": {"loc": [], "mi": []},
    "Expert-role": {"loc": [], "mi": []},
    "Student-role": {"loc": [], "mi": []},
    "Naive": {"loc": [], "mi": []},
    "Iterative": {"loc": [], "mi": []},
    "Combined": {"loc": [], "mi": []},
}

chatgpt_metrics = {
    "Zero-shot": {"loc": [], "mi": []},
    "Zero-shot-CoT": {"loc": [], "mi": []},
    "Expert-role": {"loc": [], "mi": []},
    "Student-role": {"loc": [], "mi": []},
    "Naive": {"loc": [], "mi": []},
    "Iterative": {"loc": [], "mi": []},
    "Combined": {"loc": [], "mi": []},
}

gemma_metrics = {
    "Zero-shot": {"loc": [], "mi": []},
    "Zero-shot-CoT": {"loc": [], "mi": []},
    "Expert-role": {"loc": [], "mi": []},
    "Student-role": {"loc": [], "mi": []},
    "Naive": {"loc": [], "mi": []},
    "Iterative": {"loc": [], "mi": []},
    "Combined": {"loc": [], "mi": []},
}

# Aggregate metrics data by technique for each model
for folder, stats in results_gemini.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        gemini_metrics["Zero-shot"]["loc"].append(stats['average_loc'])
        gemini_metrics["Zero-shot"]["mi"].append(stats['average_mi'])
    elif "Zero-shot-CoT" in folder:
        gemini_metrics["Zero-shot-CoT"]["loc"].append(stats['average_loc'])
        gemini_metrics["Zero-shot-CoT"]["mi"].append(stats['average_mi'])
    elif "Expert-role" in folder:
        gemini_metrics["Expert-role"]["loc"].append(stats['average_loc'])
        gemini_metrics["Expert-role"]["mi"].append(stats['average_mi'])
    elif "Student-role" in folder:
        gemini_metrics["Student-role"]["loc"].append(stats['average_loc'])
        gemini_metrics["Student-role"]["mi"].append(stats['average_mi'])
    elif "Naive" in folder:
        gemini_metrics["Naive"]["loc"].append(stats['average_loc'])
        gemini_metrics["Naive"]["mi"].append(stats['average_mi'])
    elif "Iterative" in folder:
        gemini_metrics["Iterative"]["loc"].append(stats['average_loc'])
        gemini_metrics["Iterative"]["mi"].append(stats['average_mi'])
    elif "Combined" in folder:
        gemini_metrics["Combined"]["loc"].append(stats['average_loc'])
        gemini_metrics["Combined"]["mi"].append(stats['average_mi'])

for folder, stats in results_chatgpt.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_metrics["Zero-shot"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Zero-shot"]["mi"].append(stats['average_mi'])
    elif "Zero-shot-CoT" in folder:
        chatgpt_metrics["Zero-shot-CoT"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Zero-shot-CoT"]["mi"].append(stats['average_mi'])
    elif "Expert-role" in folder:
        chatgpt_metrics["Expert-role"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Expert-role"]["mi"].append(stats['average_mi'])
    elif "Student-role" in folder:
        chatgpt_metrics["Student-role"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Student-role"]["mi"].append(stats['average_mi'])
    elif "Naive" in folder:
        chatgpt_metrics["Naive"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Naive"]["mi"].append(stats['average_mi'])
    elif "Iterative" in folder:
        chatgpt_metrics["Iterative"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Iterative"]["mi"].append(stats['average_mi'])
    elif "Combined" in folder:
        chatgpt_metrics["Combined"]["loc"].append(stats['average_loc'])
        chatgpt_metrics["Combined"]["mi"].append(stats['average_mi'])

for folder, stats in results_gemma.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        gemma_metrics["Zero-shot"]["loc"].append(stats['average_loc'])
        gemma_metrics["Zero-shot"]["mi"].append(stats['average_mi'])
    elif "Zero-shot-CoT" in folder:
        gemma_metrics["Zero-shot-CoT"]["loc"].append(stats['average_loc'])
        gemma_metrics["Zero-shot-CoT"]["mi"].append(stats['average_mi'])
    elif "Expert-role" in folder:
        gemma_metrics["Expert-role"]["loc"].append(stats['average_loc'])
        gemma_metrics["Expert-role"]["mi"].append(stats['average_mi'])
    elif "Student-role" in folder:
        gemma_metrics["Student-role"]["loc"].append(stats['average_loc'])
        gemma_metrics["Student-role"]["mi"].append(stats['average_mi'])
    elif "Naive" in folder:
        gemma_metrics["Naive"]["loc"].append(stats['average_loc'])
        gemma_metrics["Naive"]["mi"].append(stats['average_mi'])
    elif "Iterative" in folder:
        gemma_metrics["Iterative"]["loc"].append(stats['average_loc'])
        gemma_metrics["Iterative"]["mi"].append(stats['average_mi'])
    elif "Combined" in folder:
        gemma_metrics["Combined"]["loc"].append(stats['average_loc'])
        gemma_metrics["Combined"]["mi"].append(stats['average_mi'])

# Print average metrics by technique for each model
print("\nGemini Metrics Averages by Technique:")
for technique, metrics in gemini_metrics.items():
    if metrics["loc"] and metrics["mi"]:
        avg_loc = statistics.mean(metrics["loc"])
        avg_mi = statistics.mean(metrics["mi"])
        print(f"  {technique}: Average LOC = {avg_loc:.2f}, Average MI = {avg_mi:.2f}")
    else:
        print(f"  {technique}: No data available.")

print("\nChatGPT Metrics Averages by Technique:")
for technique, metrics in chatgpt_metrics.items():
    if metrics["loc"] and metrics["mi"]:
        avg_loc = statistics.mean(metrics["loc"])
        avg_mi = statistics.mean(metrics["mi"])
        print(f"  {technique}: Average LOC = {avg_loc:.2f}, Average MI = {avg_mi:.2f}")
    else:
        print(f"  {technique}: No data available.")

print("\nGemma3 Metrics Averages by Technique:")
for technique, metrics in gemma_metrics.items():
    if metrics["loc"] and metrics["mi"]:
        avg_loc = statistics.mean(metrics["loc"])
        avg_mi = statistics.mean(metrics["mi"])
        print(f"  {technique}: Average LOC = {avg_loc:.2f}, Average MI = {avg_mi:.2f}")
    else:
        print(f"  {technique}: No data available.")


# Generate table-friendly output format for both LOC and MI
print("\nTable-Ready Data (CSV format):")
print("Model,Technique,Average LOC,Median LOC,Min LOC,Max LOC,Total LOC,Average MI,Median MI,Min MI,Max MI,File Count")

def get_model_and_technique(folder_name):
    if "Gemini" in folder_name:
        model = "Gemini"
        technique = folder_name.replace("Gemini classEval ", "").replace("Gemini APPS ", "")
    elif "ChatGPT" in folder_name:
        model = "ChatGPT"
        technique = folder_name.replace("ChatGPT classEval ", "").replace("ChatGPT APPS ", "")
    elif "Gemma3" in folder_name:
        model = "Gemma3"
        technique = folder_name.replace("Gemma3 classEval ", "").replace("Gemma3 APPS ", "")
    else:
        model = "Unknown"
        technique = "Unknown"
    return model, technique

# Print data for all models and techniques based on result_setting
for folder, stats in sorted(results_gemini.items()):
    if result_setting in folder:
        model, technique = get_model_and_technique(folder)
        print(f"{model},{technique},{stats['average_loc']:.2f},{stats['median_loc']:.2f},{stats['min_loc']},{stats['max_loc']},{stats['total_loc']},{stats['average_mi']:.2f},{stats['median_mi']:.2f},{stats['min_mi']:.2f},{stats['max_mi']:.2f},{stats['file_count']}")

for folder, stats in sorted(results_chatgpt.items()):
    if result_setting in folder:
        model, technique = get_model_and_technique(folder)
        print(f"{model},{technique},{stats['average_loc']:.2f},{stats['median_loc']:.2f},{stats['min_loc']},{stats['max_loc']},{stats['total_loc']},{stats['average_mi']:.2f},{stats['median_mi']:.2f},{stats['min_mi']:.2f},{stats['max_mi']:.2f},{stats['file_count']}")

for folder, stats in sorted(results_gemma.items()):
    if result_setting in folder:
        model, technique = get_model_and_technique(folder)
        print(f"{model},{technique},{stats['average_loc']:.2f},{stats['median_loc']:.2f},{stats['min_loc']},{stats['max_loc']},{stats['total_loc']},{stats['average_mi']:.2f},{stats['median_mi']:.2f},{stats['min_mi']:.2f},{stats['max_mi']:.2f},{stats['file_count']}")



print("\nTotal Standard and Public Library Calls per Folder:")
for folder, total_calls in results_gemini.items():
    print(f"  {folder}: {total_calls['average_mi']:.2f}")

for folder, total_calls in results_chatgpt.items():
    print(f"  {folder}: {total_calls['average_mi']:.2f}")

for folder, total_calls in results_gemma.items():
    print(f"  {folder}: {total_calls['average_mi']:.2f}")
        
for folder, total_calls in ground_truth.items():
        print(f"  {folder}: {total_calls['average_mi']:.2f}")