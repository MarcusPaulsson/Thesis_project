import ast
import collections
import os
import sys
import re
import statistics

def get_loaded_modules():
    """Gets a list of all currently loaded modules."""
    return list(sys.modules.keys())

def count_library_calls(code_string):
    """Counts library calls (standard and external) in a code string."""
    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        return None, f"Error: Syntax error in code string: {e}"

    loaded_modules = get_loaded_modules()
    library_counts = collections.Counter()
    local_methods = set()
    imported_modules = set()

    # Find class and function definitions to exclude local methods
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            local_methods.add(node.name)
        elif isinstance(node, ast.ClassDef):
            for body_node in node.body:
                if isinstance(body_node, ast.FunctionDef):
                    local_methods.add(body_node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imported_modules.add(node.module)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                # Direct calls (e.g., print())
                if node.func.id in loaded_modules:
                    library_counts[node.func.id] += 1
            elif isinstance(node.func, ast.Attribute):
                # Attribute calls (e.g., os.path.join())
                try:
                    module_name = node.func.value.id
                    attribute_name = node.func.attr
                    full_name = module_name + "." + attribute_name
                    if module_name in loaded_modules:
                        library_counts[full_name] += 1
                    elif module_name in imported_modules:
                        # Attempt to capture built-in method calls (limited).
                        # Only count if the attribute is not a local method.
                        if attribute_name not in local_methods:
                            library_counts[attribute_name] += 1
                except AttributeError:
                    # Handles more complex attribute calls.
                    pass
    return library_counts, None

def numerical_sort_key(filename):
    """Sort filenames numerically if possible, otherwise alphabetically."""
    parts = re.split(r'(\d+)', filename)
    return [(int(part) if part.isdigit() else part.lower()) for part in parts]

def analyze_folders_and_count_calls(folder_paths):
    """Analyzes folders and counts library calls in Python files."""
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

        total_calls = 0
        for filename in all_file_names:
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r") as f:
                    code_string = f.read()
                counts, error = count_library_calls(code_string)
                if error:
                    print(f"Error analyzing {filename}: {error}")
                    continue
                total_calls += sum(counts.values()) if counts else 0
            except Exception as e:
                print(f"Error analyzing {filename}: {e}")
                continue

        results[folder_name] = total_calls
    return results

# Define folder paths
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) #adjust if running locally.

result_setting = "filtered_results" # "results"
folder_paths_gemini_cli_games = {
    "Gemini cli_games Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Zero-shot"),
    "Gemini cli_games Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Zero-shot-CoT"),
    "Gemini cli_games Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Expert-role"),
    "Gemini cli_games Student-role": os.path.join(upper_dir, result_setting, "Gemini", "cli_games", "Student-role"),
}

folder_paths_chatgpt_cli_games = {
    "ChatGPT cli_games Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Zero-shot"),
    "ChatGPT cli_games Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Zero-shot-CoT"),
    "ChatGPT cli_games Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Expert-role"),
    "ChatGPT cli_games Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "cli_games", "Student-role"),
}

folder_paths_gemini_classEval = {
    "Gemini classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot"),
    "Gemini classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Zero-shot-CoT"),
    "Gemini classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Expert-role"),
    "Gemini classEval Student-role": os.path.join(upper_dir, result_setting, "Gemini", "classEval", "Student-role"),
}

folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Meta": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Meta'),
    "ChatGPT classEval Naive": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Naive'),
}

folder_paths_chatgpt_APPS = {
    "ChatGPT APPS Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Zero-shot"),
    "ChatGPT APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Zero-shot-CoT"),
    "ChatGPT APPS Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Expert-role"),
    "ChatGPT APPS Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Student-role"),
    "ChatGPT APPS Meta": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Meta"),
    "ChatGPT APPS Naive": os.path.join(upper_dir, result_setting, "ChatGPT", "APPS", "Naive"),
}

folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Student-role"),
}

# Analyze folders and count library calls
results_gemini = analyze_folders_and_count_calls(folder_paths_gemini_cli_games)
results_chatgpt = analyze_folders_and_count_calls(folder_paths_chatgpt_cli_games)
results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_classEval))
results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_classEval))
results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_APPS))
results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_APPS))

print("\nTotal Library Call Counts per prompt technique:")

# Split call count calculation by technique
gemini_calls = {
    "Zero-shot": 0,
    "Zero-shot-CoT": 0,
    "Expert-role": 0,
    "Student-role": 0,
}

chatgpt_calls = {
    "Zero-shot": 0,
    "Zero-shot-CoT": 0,
    "Expert-role": 0,
    "Student-role": 0,
}

for folder, total_calls in results_gemini.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        gemini_calls["Zero-shot"] += total_calls
    elif "Zero-shot-CoT" in folder:
        gemini_calls["Zero-shot-CoT"] += total_calls
    elif "Expert-role" in folder:
        gemini_calls["Expert-role"] += total_calls
    elif "Student-role" in folder:
        gemini_calls["Student-role"] += total_calls

for folder, total_calls in results_chatgpt.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_calls["Zero-shot"] += total_calls
    elif "Zero-shot-CoT" in folder:
        chatgpt_calls["Zero-shot-CoT"] += total_calls
    elif "Expert-role" in folder:
        chatgpt_calls["Expert-role"] += total_calls
    elif "Student-role" in folder:
        chatgpt_calls["Student-role"] += total_calls

print("Gemini Total Library Calls:")
for technique, count in gemini_calls.items():
    print(f"  {technique}: {count}")

print("\nChatGPT Total Library Calls:")
for technique, count in chatgpt_calls.items():
    print(f"  {technique}: {count}")

print("\nTotal Library Calls per Folder:")
for folder, total_calls in results_gemini.items():
    print(f"  {folder}: {total_calls}")

for folder, total_calls in results_chatgpt.items():
    print(f"  {folder}: {total_calls}")