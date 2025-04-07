import ast
import builtins
import sys
import os
import re
import inspect  # To help identify standard libraries (can be tricky)
import collections

def get_standard_libraries():
    """Gets a set of standard library module names."""
    stdlib_paths = [os.path.dirname(p) for p in sys.path if 'site-packages' not in p]
    stdlib_modules = set()
    for path in stdlib_paths:
        if os.path.isdir(path):
            for item in os.listdir(path):
                if item.endswith(".py") and item != "__init__.py":
                    stdlib_modules.add(item[:-3])
                elif os.path.isdir(os.path.join(path, item)) and "__init__.py" in os.listdir(os.path.join(path, item)):
                    stdlib_modules.add(item)
    return stdlib_modules

STANDARD_LIBRARIES = get_standard_libraries()
BUILTIN_NAMES = dir(builtins)

def analyze_dependency(node, scope, module_context):
    dependencies = {"self-contained": set(), "slib-runnable": set(), "plib-runnable": set(),
                    "class-runnable": set(), "file-runnable": set(), "project-runnable": set()}

    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
        name = node.id
        if name in BUILTIN_NAMES:
            dependencies["self-contained"].add(name)
        elif name in scope['file'] and name not in scope['class']:
            dependencies["file-runnable"].add(name)
        elif name in scope['class']:
            dependencies["class-runnable"].add(name)
        elif name in module_context['imported_modules']:
            if module_context['imported_modules'][name] in STANDARD_LIBRARIES:
                dependencies["slib-runnable"].add(name)
            else:
                dependencies["plib-runnable"].add(name)
        elif name in module_context['project_level_names']:
            dependencies["project-runnable"].add(name)

    elif isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
        value = node.value
        attr = node.attr
        if isinstance(value, ast.Name):
            module_name = value.id
            full_name = f"{module_name}.{attr}"
            if module_name in module_context['imported_modules']:
                if module_context['imported_modules'][module_name] in STANDARD_LIBRARIES:
                    dependencies["slib-runnable"].add(full_name)
                else:
                    dependencies["plib-runnable"].add(full_name)
            elif module_name == 'self' and attr in scope['class_attributes']:
                dependencies["class-runnable"].add(attr)
            elif module_name in scope['file']: # Could be a module alias
                dependencies["file-runnable"].add(full_name)
            elif module_name in module_context['project_level_names']:
                dependencies["project-runnable"].add(full_name)
        # Handle more complex attribute accesses if needed

    elif isinstance(node, ast.Call):
        func = node.func
        if isinstance(func, ast.Name):
            name = func.id
            if name in BUILTIN_NAMES:
                dependencies["self-contained"].add(name + "()")
            elif name in scope['file'] and name not in scope['class']:
                dependencies["file-runnable"].add(name + "()")
            elif name in scope['class']:
                dependencies["class-runnable"].add(name + "()")
            elif name in module_context['imported_modules']:
                if module_context['imported_modules'][name] in STANDARD_LIBRARIES:
                    dependencies["slib-runnable"].add(name + "()")
                else:
                    dependencies["plib-runnable"].add(name + "()")
            elif name in module_context['project_level_names']:
                dependencies["project-runnable"].add(name + "()")
        elif isinstance(func, ast.Attribute):
            # Similar logic as attribute access
            pass

    return dependencies

def analyze_module(filepath):
    try:
        with open(filepath, 'r') as f:
            tree = ast.parse(f.read())
    except SyntaxError as e:
        return None, f"Error: Syntax error in {filepath}: {e}"
    except Exception as e:
        return None, f"Error reading {filepath}: {e}"

    module_context = {'imported_modules': {}, 'project_level_names': set()}
    file_level_names = set()
    class_definitions = {}

    # First pass to collect module-level information
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                module_context['imported_modules'][alias.name] = alias.name
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                module_context['imported_modules'][alias.asname if alias.asname else alias.name] = node.module
        elif isinstance(node, ast.FunctionDef):
            file_level_names.add(node.name)
        elif isinstance(node, ast.ClassDef):
            file_level_names.add(node.name)
            class_definitions[node.name] = {'methods': set(), 'attributes': set()}
            for body_node in node.body:
                if isinstance(body_node, ast.FunctionDef):
                    class_definitions[node.name]['methods'].add(body_node.name)
                elif isinstance(body_node, ast.AnnAssign) or isinstance(body_node, ast.Assign) and isinstance(body_node.targets[0], ast.Name):
                    class_definitions[node.name]['attributes'].add(body_node.targets[0].id)

    module_context['project_level_names'].update(file_level_names) # For simplicity, assuming all in the file are potentially project-level

    function_dependencies = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            scope = {'file': file_level_names, 'class': set(), 'class_attributes': set()}
            enclosing_class = None
            for ancestor in ast.walk(tree):
                if isinstance(ancestor, ast.ClassDef) and any(child is node for child in ancestor.body):
                    enclosing_class = ancestor.name
                    scope['class'] = class_definitions.get(enclosing_class, {}).get('methods', set())
                    scope['class_attributes'] = class_definitions.get(enclosing_class, {}).get('attributes', set())
                    break

            dependencies = {"self-contained": set(), "slib-runnable": set(), "plib-runnable": set(),
                            "class-runnable": set(), "file-runnable": set(), "project-runnable": set()}
            for child in ast.walk(node):
                dep = analyze_dependency(child, scope, module_context)
                for dep_type, names in dep.items():
                    dependencies[dep_type].update(names)
            function_dependencies[function_name] = dependencies

    return function_dependencies, None

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
            dependencies, error = analyze_module(file_path)
            if error:
                print(f"Error analyzing {filename}: {error}")
                continue
            if dependencies:
                for func_deps in dependencies.values():
                    for dep_type, names in func_deps.items():
                        if dep_type in ["slib-runnable", "plib-runnable"]:
                            total_calls += len(names)
        results[folder_name] = total_calls
    return results

# Define folder paths
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) #adjust if running locally.

result_setting = "results" # "results"
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
}
folder_paths_chatgpt_classEval = {
    "ChatGPT classEval Zero-shot": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot"),
    "ChatGPT classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Zero-shot-CoT"),
    "ChatGPT classEval Expert-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Expert-role"),
    "ChatGPT classEval Student-role": os.path.join(upper_dir, result_setting, "ChatGPT", "classEval", "Student-role"),
    "ChatGPT classEval Meta": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Meta'),
    "ChatGPT classEval Naive": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Naive'),
    "ChatGPT classEval Iterative": os.path.join(upper_dir,result_setting, 'ChatGPT', 'classEval', 'Iterative'),
}
folder_paths_gemma_classEval = {
    "Gemma3 classEval Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot"),
    "Gemma3 classEval Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Zero-shot-CoT"),
    "Gemma3 classEval Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Expert-role"),
    "Gemma3 classEval Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Student-role"),
    "Gemma3 classEval Meta": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Meta"),
    "Gemma3 classEval Naive": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Naive"),
    "Gemma3 classEval Iterative": os.path.join(upper_dir, result_setting, "Gemma3", "classEval", "Iterative"),
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
}
folder_paths_gemini_APPS = {
    "Gemini APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot"),
    "Gemini APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Zero-shot-CoT"),
    "Gemini APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Expert-role"),
    "Gemini APPS Student-role": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Student-role"),
    "Gemini APPS Meta": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Meta"),
    "Gemini APPS Naive": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Naive"),
    "Gemini APPS Iterative": os.path.join(upper_dir, result_setting, "Gemini", "APPS", "Iterative"),
}
folder_paths_gemma_APPS = {
    "Gemma3 APPS Zero-shot": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot"),
    "Gemma3 APPS Zero-shot-CoT": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Zero-shot-CoT"),
    "Gemma3 APPS Expert-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Expert-role"),
    "Gemma3 APPS Student-role": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Student-role"),
    "Gemma3 APPS Meta": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Meta"),
    "Gemma3 APPS Naive": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Naive"),
    "Gemma3 APPS Iterative": os.path.join(upper_dir, result_setting, "Gemma3", "APPS", "Iterative"),
}

# Analyze folders and count library calls (using the new logic which focuses on slib and plib)
results_gemini = {}
results_chatgpt = {}
results_gemma = {}

results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_APPS))
results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_classEval))

results_gemma.update(analyze_folders_and_count_calls(folder_paths_gemma_classEval))
results_gemma.update(analyze_folders_and_count_calls(folder_paths_gemma_APPS))

results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_APPS))
results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_classEval))

print("\nTotal Standard and Public Library Call Counts per prompt technique:")
gemini_calls = {  # Split call count calculation by technique
    "Zero-shot": 0,
    "Zero-shot-CoT": 0,
    "Expert-role": 0,
    "Student-role": 0,
    "Meta": 0,
    "Naive": 0,
    "Iterative": 0,
}

chatgpt_calls = {
    "Zero-shot": 0,
    "Zero-shot-CoT": 0,
    "Expert-role": 0,
    "Student-role": 0,
    "Meta": 0,
    "Naive": 0,
    "Iterative": 0,
}

gemma_calls = {
    "Zero-shot": 0,
    "Zero-shot-CoT": 0,
    "Expert-role": 0,
    "Student-role": 0,
    "Meta": 0,
    "Naive": 0,
    "Iterative": 0,
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
    elif "Meta" in folder:
        gemini_calls["Meta"] += total_calls
    elif "Naive" in folder:
        gemini_calls["Naive"] += total_calls
    elif "Iterative" in folder:
        gemini_calls["Iterative"] += total_calls

for folder, total_calls in results_chatgpt.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_calls["Zero-shot"] += total_calls
    elif "Zero-shot-CoT" in folder:
        chatgpt_calls["Zero-shot-CoT"] += total_calls
    elif "Expert-role" in folder:
        chatgpt_calls["Expert-role"] += total_calls
    elif "Student-role" in folder:
        chatgpt_calls["Student-role"] += total_calls
    elif "Meta" in folder:
        chatgpt_calls["Meta"] += total_calls
    elif "Naive" in folder:
        chatgpt_calls["Naive"] += total_calls
    elif "Iterative" in folder:
        chatgpt_calls["Iterative"] += total_calls

for folder, total_calls in results_gemma.items():
    if "Zero-shot" in folder and "CoT" not in folder:
        chatgpt_calls["Zero-shot"] += total_calls
    elif "Zero-shot-CoT" in folder:
        chatgpt_calls["Zero-shot-CoT"] += total_calls
    elif "Expert-role" in folder:
        chatgpt_calls["Expert-role"] += total_calls
    elif "Student-role" in folder:
        chatgpt_calls["Student-role"] += total_calls
    elif "Meta" in folder:
        chatgpt_calls["Meta"] += total_calls
    elif "Naive" in folder:
        chatgpt_calls["Naive"] += total_calls
    elif "Iterative" in folder:
        chatgpt_calls["Iterative"] += total_calls

print("Gemini Total Standard and Public Library Calls:")
for technique, count in gemini_calls.items():
    print(f"  {technique}: {count}")

print("\nChatGPT Total Standard and Public Library Calls:")
for technique, count in chatgpt_calls.items():
    print(f"  {technique}: {count}")

print("\Gemma3 Total Standard and Public Library Calls:")
for technique, count in results_gemma.items():
    print(f"  {technique}: {count}")


print("\nTotal Standard and Public Library Calls per Folder:")
for folder, total_calls in results_gemini.items():
    print(f"  {folder}: {total_calls}")

for folder, total_calls in results_chatgpt.items():
    print(f"  {folder}: {total_calls}")

for folder, total_calls in results_gemma.items():
    print(f"  {folder}: {total_calls}")