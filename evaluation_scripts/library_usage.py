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

BUILTIN_NAMES = set(dir(builtins))
BUILTIN_NAMES= BUILTIN_NAMES.union(set(dir(inspect)))



def analyze_dependency(node, scope, module_context):
    """Analyzes the dependencies of a node in the AST."""
    dependencies = {"self-contained": set(), "slib-runnable": set(), "plib-runnable": set(),
                    "class-runnable": set(), "file-runnable": set(), "project-runnable": set(),
                    "builtin-used": set()}  # Added 'builtin-used'

    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
        name = node.id
        if name in BUILTIN_NAMES:
            dependencies["builtin-used"].add(name)
        elif name in scope['file'] and name not in scope['class']:
            dependencies["file-runnable"].add(name)
        elif name in scope['class']:
            dependencies["class-runnable"].add(name)
        # We only consider direct name access as a runnable dependency if it's a function call (handled below)
        elif name in module_context['imported_modules']:
            pass # Do not add the module name itself as a runnable dependency
        elif name in module_context['project_level_names']:
            dependencies["project-runnable"].add(name)

    elif isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
        value = node.value
        attr = node.attr
        if isinstance(value, ast.Name):
            module_name = value.id
            full_name = f"{module_name}.{attr}"
            if module_name in module_context['imported_modules']:
                imported_module = module_context['imported_modules'][module_name]
                if imported_module in STANDARD_LIBRARIES:
                    dependencies["slib-runnable"].add(full_name)
                else:
                    dependencies["plib-runnable"].add(full_name)
            elif module_name == 'self' and attr in scope['class_attributes']:
                dependencies["class-runnable"].add(attr)
            elif module_name in scope['file']: # Could be a module alias
                dependencies["file-runnable"].add(full_name)
            elif module_name in module_context['project_level_names']:
                dependencies["project-runnable"].add(full_name)

    elif isinstance(node, ast.Call):
        func = node.func
        if isinstance(func, ast.Name):
            name = func.id
            if name in BUILTIN_NAMES:
                dependencies["builtin-used"].add(name + "()")
            elif name in scope['file'] and name not in scope['class']:
                dependencies["file-runnable"].add(name + "()")
            elif name in scope['class']:
                dependencies["class-runnable"].add(name + "()")
            elif name in module_context['imported_modules']:
                imported_module = module_context['imported_modules'][name]
                if imported_module in STANDARD_LIBRARIES:
                    dependencies["slib-runnable"].add(name + "()")
                else:
                    dependencies["plib-runnable"].add(name + "()")
            elif name in module_context['project_level_names']:
                dependencies["project-runnable"].add(name + "()")
        elif isinstance(func, ast.Attribute):
            # Attribute calls (e.g., json.load()) are already handled above
            pass

    return dependencies

def analyze_module(filepath):
    """Analyzes a single Python module for function dependencies."""
    try:
        with open(filepath, 'r') as f:
            tree = ast.parse(f.read())
    except SyntaxError as e:
        return None, f"Error: Syntax error in {filepath}: {e}"
    except Exception as e:
        return None, f"Error reading {filepath}: {e}"

    module_context = {'imported_modules': {}, 'imported_modules_used': set(), 'project_level_names': set()}
    file_level_names = set()
    class_definitions = {}

    # First pass to collect module-level information (imports and definitions)
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
                            "class-runnable": set(), "file-runnable": set(), "project-runnable": set(),
                            "builtin-used": set()} # Added 'builtin-used'
            for child in ast.walk(node):
                dep = analyze_dependency(child, scope, module_context)
                for dep_type, names in dep.items():
                    dependencies[dep_type].update(names)

            # Update imported_modules_used based on the dependencies found in this function
            for dep_type in ["slib-runnable", "plib-runnable", "builtin-used" ]:
            #for dep_type in ["slib-runnable", "plib-runnable", "builtin-used","class-runnable", "file-runnable" , "project-runnable","self-contained"]:
                for name in dependencies[dep_type]:
                    if '.' in name:
                        module_alias = name.split('.')[0]
                    else:
                        module_alias = name
                    if module_alias in module_context['imported_modules']:
                        module_context['imported_modules_used'].add(module_alias)


            builtins_to_remove = set()
            for item in dependencies["builtin-used"]:
                if not item.endswith("()"):
                    builtins_to_remove.add(item)

            dependencies["builtin-used"] -= builtins_to_remove
            
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
                        if dep_type in ["slib-runnable", "plib-runnable", "builtin-used" ]:
                        #if dep_type in ["slib-runnable", "plib-runnable", "builtin-used", "class-runnable", "file-runnable" , "project-runnable" ,"self-contained"]:
                            total_calls += len(names)
                            
        results[folder_name] = total_calls
    return results

if __name__ == "__main__":
    # Define folder paths
    upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) #adjust if running locally.

    filtered = False
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

    # Analyze folders and count library calls (using the new logic which focuses on slib and plib)
    results_gemini = {}
    results_chatgpt = {}
    results_gemma = {}
    ground_truth = {}

    results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_APPS))
    results_gemini.update(analyze_folders_and_count_calls(folder_paths_gemini_classEval))

    results_gemma.update(analyze_folders_and_count_calls(folder_paths_gemma_classEval))
    results_gemma.update(analyze_folders_and_count_calls(folder_paths_gemma_APPS))

    results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_APPS))
    results_chatgpt.update(analyze_folders_and_count_calls(folder_paths_chatgpt_classEval))

    ground_truth.update(analyze_folders_and_count_calls(folder_paths_ground_truth_classEval))
    ground_truth.update(analyze_folders_and_count_calls(folder_paths_ground_truth_APPS))


    print("\nTotal Standard and Public Library Calls per Folder:")
    for folder, total_calls in results_gemini.items():
        print(f"  {folder}: {total_calls}")

    for folder, total_calls in results_chatgpt.items():
        print(f"  {folder}: {total_calls}")

    for folder, total_calls in results_gemma.items():
        print(f"  {folder}: {total_calls}")
        
    for folder, total_calls in ground_truth.items():
        print(f"  {folder}: {total_calls}")

run_on_single_file = False
if run_on_single_file:
    # Define the path to the file you want to analyze
    upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath_to_analyze = os.path.join(upper_dir, "filtered_results", "ChatGPT", "classEval", "Iterative", "code_18.py")

    function_dependencies, error = analyze_module(filepath_to_analyze)

    print(f"\nAnalysis of '{filepath_to_analyze}':\n")
    if error:
        print(f"Error: {error}")
    elif function_dependencies:
        overall_counts = {
            "self-contained": 0,
            "slib-runnable": 0,
            "plib-runnable": 0,
            "class-runnable": 0,
            "file-runnable": 0,
            "project-runnable": 0,
            "builtin-used": 0,
        }

        for function_name, dependencies in function_dependencies.items():
            print(f"Function: {function_name}")
            slib_count = len(dependencies.get("slib-runnable", set()))
            plib_count = len(dependencies.get("plib-runnable", set()))
            builtin_count = len(dependencies.get("builtin-used", set()))
            class_count = len(dependencies.get("class-runnable", set()))
            file_count = len(dependencies.get("file-runnable", set()))
            project_count = len(dependencies.get("project-runnable", set()))
            self_contained_count = len(dependencies.get("self-contained", set()))

            overall_counts["slib-runnable"] += slib_count
            overall_counts["plib-runnable"] += plib_count
            overall_counts["builtin-used"] += builtin_count
            overall_counts["class-runnable"] += class_count
            overall_counts["file-runnable"] += file_count
            overall_counts["project-runnable"] += project_count
            overall_counts["self-contained"] += self_contained_count

            for dep_type, names in dependencies.items():
                if names:
                    print(f"  {dep_type.replace('-', ' ').title()}: {', '.join(sorted(list(names)))}")
            print(f"  Function Standard Library Calls: {slib_count}")
            print(f"  Function Public Library Calls: {plib_count}")
            print(f"  Function Built-in Calls: {builtin_count}")
            print(f"  Function Class Runnable Calls: {class_count}")
            print(f"  Function File Runnable Calls: {file_count}")
            print(f"  Function Project Runnable Calls: {project_count}")
            print(f"  Function Self-Contained Calls: {self_contained_count}\n")

        print(f"\nOverall Counts for '{filepath_to_analyze}':")
        print(f"  Total Standard Library Calls: {overall_counts['slib-runnable']}")
        print(f"  Total Public Library Calls: {overall_counts['plib-runnable']}")
        print(f"  Total Built-in Calls: {overall_counts['builtin-used']}")
        print(f"  Total Class Runnable Calls: {overall_counts['class-runnable']}")
        print(f"  Total File Runnable Calls: {overall_counts['file-runnable']}")
        print(f"  Total Project Runnable Calls: {overall_counts['project-runnable']}")
        print(f"  Total Self-Contained Calls: {overall_counts['self-contained']}")

    else:
        print("No functions found in the file.")