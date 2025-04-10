import os
import json
import subprocess
import sys
import tempfile
import shutil

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)

# Gemini
Gemini_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Zero-shot'))
Gemini_zero_shot_CoT_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Zero-shot-CoT'))
Gemini_student_role_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Student-role'))
Gemini_expert_role_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Expert-role'))
Gemini_meta_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Meta'))
Gemini_naive_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Naive'))
Gemini_iterative_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Iterative'))
Gemini_combined_apps_folder = os.path.abspath(os.path.join('results', 'Gemini', 'APPS', 'Combined'))

# ChatGPT
chatGPT_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot'))
chatGPT_zero_shot_CoT_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot-CoT'))
chatGPT_student_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Student-role'))
chatGPT_expert_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Expert-role'))
chatGPT_meta_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Meta'))
chatGPT_naive_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Naive'))
chatGPT_iterative_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Iterative'))
chatGPT_combined_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Combined'))

# Gemma
gemma_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Zero-shot'))
gemma_zero_shot_CoT_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Zero-shot-CoT'))
gemma_student_role_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Student-role'))
gemma_expert_role_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Expert-role'))
gemma_meta_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Meta'))
gemma_naive_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Naive'))
gemma_iterative_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Iterative'))
gemma_combined_apps_folder = os.path.abspath(os.path.join('results', 'Gemma3', 'APPS', 'Combined'))

# WizardCoder
#wizardCoder_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'WizardCoder', 'APPS', 'Zero-shot'))

# Qwen
#qwen_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'Qwen', 'APPS', 'Zero-shot'))






# Define a list of folder paths and their corresponding names
folder_paths = {

     "Gemini Zero-shot": Gemini_zero_shot_apps_folder,
     "Gemini Zero-shot-CoT": Gemini_zero_shot_CoT_apps_folder,
     "Gemini Student-role": Gemini_student_role_apps_folder,
     "Gemini Expert-role": Gemini_expert_role_apps_folder,
     "Gemini Meta": Gemini_meta_apps_folder,
     "Gemini Naive": Gemini_naive_apps_folder,
     "Gemini Iterative": Gemini_iterative_apps_folder,
     "Gemini Combined": Gemini_combined_apps_folder,

     "ChatGPT Zero-shot": chatGPT_zero_shot_apps_folder,
     "ChatGPT Zero-shot-CoT": chatGPT_zero_shot_CoT_apps_folder,
     "ChatGPT Student-role": chatGPT_student_role_apps_folder,
     "ChatGPT Expert-role": chatGPT_expert_role_apps_folder,
     "ChatGPT Meta": chatGPT_meta_apps_folder,
     "ChatGPT Naive": chatGPT_naive_apps_folder,
     "ChatGPT Iterative": chatGPT_iterative_apps_folder,
     "ChatGPT Combined": chatGPT_combined_apps_folder,

    "Gemma3 Zero-shot": gemma_zero_shot_apps_folder,
    "Gemma3 Zero-shot-CoT": gemma_zero_shot_CoT_apps_folder,
    "Gemma3 Student-role": gemma_student_role_apps_folder,
    "Gemma3 Expert-role": gemma_expert_role_apps_folder,
    "Gemma3 Meta": gemma_meta_apps_folder,
    "Gemma3 Naive": gemma_naive_apps_folder,
    "Gemma3 Iterative": gemma_iterative_apps_folder,
    "Gemma3 Combined": gemma_combined_apps_folder,

}


test_data_path = os.path.abspath(os.path.join('data', 'apps.json'))

def load_apps_tests(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            return [json.loads(line.strip()) for line in jsonfile if "input_output" in json.loads(line.strip())]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

def run_tests_on_code_snippets(tasks, folder_path, temp_dir):
    if not tasks:
        return {"passed": 0, "total": 0, "passed_ids": []}

    passed_tests = 0
    total_tests = 100
    passed_ids = []
    for i, task_data in enumerate(tasks):
        task = task_data["input_output"]

        # Extract task_id from the filename
        file_name = f"code_{i}.py"
        try:
            code_id = int(file_name.split("_")[1].split(".")[0])
        except (IndexError, ValueError):
            print(f"Warning: Could not extract task_id from filename '{file_name}'. Skipping test.")
            continue

        file_path = os.path.join(folder_path, f"code_{i}.py")
        if not os.path.exists(file_path):
            print(f"Warning: File '{file_path}' not found for test {i + 1}.")
            continue

        try:
            with open(file_path, 'r') as f:
                generated_code = f.read()

            temp_file_path = os.path.join(temp_dir, f"temp_test_{i}.py")
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(generated_code)

            print(f"\n--- Running Test {i + 1} of {total_tests} ---")
            json_data = json.loads(task)
            inputs, outputs = json_data["inputs"], json_data["outputs"]
            max_numb_test, placeholder = 5, 5
            output_list = []
            for test_i, item in enumerate(inputs):
                if max_numb_test:
                    max_numb_test -= 1
                else:
                    break
                process = subprocess.Popen(["python", temp_file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                stdout, stderr = process.communicate(item, timeout=5)
                output_list.append(stdout[:-1])
                output_list
            if process.returncode == 0:
                expected_lines = outputs[:placeholder]
                expected_lines = [item.strip() for item in expected_lines]

                if output_list == expected_lines:
                    print(f"Test {i + 1} passed")
                    passed_tests += 1
                    passed_ids.append(code_id)
                else:
                    print(f"Test {i + 1} failed: Output mismatch")
                    print(f"Expected: {expected_lines}")
                    print(f"Actual: {output_list}")
                    print(f"Stderr: {stderr}")
                    print(f"Stdout: {stdout}")
            else:
                print(f"Test {i + 1} failed: Runtime error")
                print(f"Stderr: {stderr}")
                print(f"Stdout: {stdout}")

        except subprocess.TimeoutExpired:
            print(f"Test {i + 1} timed out.")
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Error: {e}")

    print(f"\n--- Test Summary ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    return {"passed": passed_tests, "total": total_tests, "passed_ids": passed_ids}

tasks = load_apps_tests(test_data_path)


def extract_and_save_passed_code(passed_code_ids):
    
    dir = os.path.abspath(os.path.join(upper_dir,'filtered_results')) # Flush previous folder for storing and make a new fresh.
    os.makedirs(dir, exist_ok=True)

    for passed_index in passed_code_ids:
        for i in folder_paths:
            parts = folder_paths[i].split(os.sep)  # Split the path into its components
            if parts[-4] == 'results':
                parts[-4] = 'filtered_results'
                filtered_folder_path = os.path.join(*parts[-4:])
                filename_to_copy = f"code_{passed_index}.py"
                source_file_path = os.path.join(folder_paths[i], filename_to_copy)
                destination_file_path = os.path.join(filtered_folder_path, filename_to_copy)
                os.makedirs(filtered_folder_path, exist_ok=True)
                shutil.copy2(source_file_path, destination_file_path) # copy with metadata


save_passed = False
if tasks:
    results = {}
    temp_dir = "tempfolder_apps"
    os.makedirs(temp_dir, exist_ok=True)

    for folder_name, folder_path in folder_paths.items():
        print(f"\n--- Running {folder_name} Tests ---")
        results[folder_name] = run_tests_on_code_snippets(tasks, folder_path, temp_dir)

    print("\n--- Overall Test Summary ---")
    total_passed = 0
    total_all = 0
    model_passed_ids = {}
    for folder, result in results.items():
        print(f"{folder}: Passed {result['passed']} of {result['total']}")
        total_passed += result['passed']
        total_all += result['total']
        model_name = folder.split()[0]
        if model_name not in model_passed_ids:
            model_passed_ids[model_name] = {}
        model_passed_ids[model_name][folder] = set(result['passed_ids'])

    print(f"\nTotal Passed: {total_passed} of {total_all}")

    venn_data = {}
    all_task_ids = set(range(len(tasks)))

    model_names = sorted(model_passed_ids.keys())

    # Calculate intersections
    if len(model_names) >= 3:
        m1, m2, m3 = model_names[0], model_names[1], model_names[2]

        # Passed by all prompt techniques for each model
        passed_all_m1 = set.intersection(*[model_passed_ids[m1][f] for f in model_passed_ids[m1]]) if m1 in model_passed_ids else set()
        passed_all_m2 = set.intersection(*[model_passed_ids[m2][f] for f in model_passed_ids[m2]]) if m2 in model_passed_ids else set()
        passed_all_m3 = set.intersection(*[model_passed_ids[m3][f] for f in model_passed_ids[m3]]) if m3 in model_passed_ids else set()

        # Intersection of all three
        venn_data[f"{m1}_and_{m2}_and_{m3}"] = len(passed_all_m1.intersection(passed_all_m2, passed_all_m3))

        # Intersection of each pair (exclusive of the third)
        venn_data[f"{m1}_and_{m2}_only"] = len(passed_all_m1.intersection(passed_all_m2) - passed_all_m3)
        venn_data[f"{m1}_and_{m3}_only"] = len(passed_all_m1.intersection(passed_all_m3) - passed_all_m2)
        venn_data[f"{m2}_and_{m3}_only"] = len(passed_all_m2.intersection(passed_all_m3) - passed_all_m1)

        # Only passed by each model (exclusive of the others)
        venn_data[f"{m1}_only"] = len(passed_all_m1 - passed_all_m2 - passed_all_m3)
        venn_data[f"{m2}_only"] = len(passed_all_m2 - passed_all_m1 - passed_all_m3)
        venn_data[f"{m3}_only"] = len(passed_all_m3 - passed_all_m1 - passed_all_m2)

        # Total passed by each model (across all techniques)
        venn_data[f"total_passed_{m1}"] = len(passed_all_m1)
        venn_data[f"total_passed_{m2}"] = len(passed_all_m2)
        venn_data[f"total_passed_{m3}"] = len(passed_all_m3)

        # Total non-passing (assuming 100 total tests)
        total_passing = (
            venn_data.get(f"{m1}_only", 0) +
            venn_data.get(f"{m2}_only", 0) +
            venn_data.get(f"{m3}_only", 0) +
            venn_data.get(f"{m1}_and_{m2}_only", 0) +
            venn_data.get(f"{m1}_and_{m3}_only", 0) +
            venn_data.get(f"{m2}_and_{m3}_only", 0) +
            venn_data.get(f"{m1}_and_{m2}_and_{m3}", 0)
        )
        venn_data["non_passing"] = 100 - total_passing
        print("\n--- Venn Diagram Data (for the first 3 models) ---")
        for key, value in venn_data.items():
            print(f"{key}: {value}")
    elif len(model_names) == 2:
        m1, m2 = model_names[0], model_names[1]
        passed_all_m1 = set.intersection(*[model_passed_ids[m1][f] for f in model_passed_ids[m1]]) if m1 in model_passed_ids else set()
        passed_all_m2 = set.intersection(*[model_passed_ids[m2][f] for f in model_passed_ids[m2]]) if m2 in model_passed_ids else set()

        venn_data[f"{m1}_and_{m2}"] = len(passed_all_m1.intersection(passed_all_m2))
        venn_data[f"{m1}_only"] = len(passed_all_m1 - passed_all_m2)
        venn_data[f"{m2}_only"] = len(passed_all_m2 - passed_all_m1)
        venn_data[f"total_passed_{m1}"] = len(passed_all_m1)
        venn_data[f"total_passed_{m2}"] = len(passed_all_m2)
        venn_data["non_passing"] = 100 - (venn_data.get(f"{m1}_only", 0) + venn_data.get(f"{m2}_only", 0) + venn_data.get(f"{m1}_and_{m2}", 0))
        print("\n--- Venn Diagram Data (for the first 2 models) ---")
        for key, value in venn_data.items():
            print(f"{key}: {value}")
    elif len(model_names) == 1:
        m1 = model_names[0]
        passed_all_m1 = set.intersection(*[model_passed_ids[m1][f] for f in model_passed_ids[m1]]) if m1 in model_passed_ids else set()
        venn_data[f"{m1}_only"] = len(passed_all_m1)
        venn_data["non_passing"] = 100 - venn_data.get(f"{m1}_only", 0)
        print("\n--- Venn Diagram Data (for the first model) ---")
        for key, value in venn_data.items():
            print(f"{key}: {value}")
    else:
        print("\n--- Not enough models to generate Venn diagram data ---")

    shutil.rmtree(temp_dir)
    if save_passed:
        # Determine codes passed by all techniques of each model
        for model in model_names:
            if model in model_passed_ids:
                passed_by_all_techniques = set.intersection(*[model_passed_ids[model][f] for f in model_passed_ids[model]])
                if passed_by_all_techniques:
                    print(f"\nSaving codes passed by all techniques of {model}: {sorted(list(passed_by_all_techniques))}")
                    extract_and_save_passed_code(list(passed_by_all_techniques))



        

    