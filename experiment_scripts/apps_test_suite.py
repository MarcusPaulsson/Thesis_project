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

# ChatGPT
chatGPT_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot'))
chatGPT_zero_shot_CoT_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot-CoT'))
chatGPT_student_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Student-role'))
chatGPT_expert_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Expert-role'))
chatGPT_meta_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Meta'))
chatGPT_naive_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Naive'))
chatGPT_iterative_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Iterative'))

# WizardCoder
wizardCoder_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'WizardCoder', 'APPS', 'Zero-shot'))

# Qwen
qwen_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'Qwen', 'APPS', 'Zero-shot'))

# Define a list of folder paths and their corresponding names
folder_paths = {

    "Gemini Zero-shot": Gemini_zero_shot_apps_folder,
    "Gemini Zero-shot-CoT": Gemini_zero_shot_CoT_apps_folder,
    "Gemini Student-role": Gemini_student_role_apps_folder,
    "Gemini Expert-role": Gemini_expert_role_apps_folder,
    "Gemini Meta": Gemini_meta_apps_folder,
    "Gemini Naive": Gemini_naive_apps_folder,
    "Gemini Iterative": Gemini_iterative_apps_folder,

    "ChatGPT Zero-shot": chatGPT_zero_shot_apps_folder,
    "ChatGPT Zero-shot-CoT": chatGPT_zero_shot_CoT_apps_folder,
    "ChatGPT Student-role": chatGPT_student_role_apps_folder,
    "ChatGPT Expert-role": chatGPT_expert_role_apps_folder,
    "ChatGPT Meta": chatGPT_meta_apps_folder,
    "ChatGPT Naive": chatGPT_naive_apps_folder,
    "ChatGPT Iterative": chatGPT_iterative_apps_folder,

    # "Qwen Zero-shot": qwen_zero_shot_apps_folder,
    # "WizardCoder Zero-shot": wizardCoder_zero_shot_apps_folder
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


save_passed = True
if tasks:
    results = {}
    temp_dir = "tempfolder"
    os.makedirs(temp_dir, exist_ok=True)

    for folder_name, folder_path in folder_paths.items():
        print(f"\n--- Running {folder_name} Tests ---")
        results[folder_name] = run_tests_on_code_snippets(tasks, folder_path, temp_dir)

    print("\n--- Overall Test Summary ---")
    total_passed = 0
    total_all = 0
    all_passed_ids = {} # Change to dict for id count
    for folder, result in results.items():
        print(f"{folder}: Passed {result['passed']} of {result['total']}")
        total_passed += result['passed']
        total_all += result['total']
        for id in result['passed_ids']:
            if id in all_passed_ids:
                all_passed_ids[id] += 1
            else:
                all_passed_ids[id] = 1

    print(f"\nTotal Passed: {total_passed} of {total_all}")

    # Find IDs that passed in all folders
    passed_in_all = [id for id, count in all_passed_ids.items() if count == len(folder_paths)]
    common_passed_code = sorted(passed_in_all)
    print(f"\nPassed in all folders: {common_passed_code}")
    shutil.rmtree(temp_dir)
    if save_passed:
        extract_and_save_passed_code(common_passed_code)



        

    