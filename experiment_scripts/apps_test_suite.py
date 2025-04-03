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

# ChatGPT
chatGPT_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot'))
chatGPT_zero_shot_CoT_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Zero-shot-CoT'))
chatGPT_student_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Student-role'))
chatGPT_expert_role_apps_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'APPS', 'Expert-role'))

# WizardCoder
wizardCoder_zero_shot_apps_folder = os.path.abspath(os.path.join('results', 'WizardCoder', 'APPS', 'Zero-shot'))

# Define a list of folder paths and their corresponding names
folder_paths = {
   # "Gemini Zero-shot": Gemini_zero_shot_apps_folder,
    #"Gemini Zero-shot-CoT": Gemini_zero_shot_CoT_apps_folder,
    "Gemini Student-role": Gemini_student_role_apps_folder,
   # "Gemini Expert-role": Gemini_expert_role_apps_folder,
   # "ChatGPT Zero-shot": chatGPT_zero_shot_apps_folder,
  #  "ChatGPT Zero-shot-CoT": chatGPT_zero_shot_CoT_apps_folder,
   # "ChatGPT Student-role": chatGPT_student_role_apps_folder,
    #"ChatGPT Expert-role": chatGPT_expert_role_apps_folder,
}

test_data_path = os.path.abspath(os.path.join('data', 'apps.json'))

def load_apps_tests(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            return [json.loads(line.strip())["input_output"] for line in jsonfile if "input_output" in json.loads(line.strip())]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

def run_tests_on_code_snippets(tasks, folder_path, temp_dir):
    if not tasks:
        return {"passed": 0, "total": 0}

    passed_tests = 0
    total_tests = min(30, len(tasks))
    for i, task in enumerate(tasks[:30]):
        file_path = os.path.join(folder_path, f"code_{i}.py")
        print(file_path)
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
            process = subprocess.Popen(["python", temp_file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input="\n".join(inputs), timeout=5)

            if process.returncode == 0:
                output_lines = [line.strip() for line in stdout.strip().split('\n')]
                expected_lines = [line.strip() for expected_output in outputs for line in expected_output.strip().split('\n')]

                if output_lines == expected_lines:
                    print(f"Test {i + 1} passed")
                    passed_tests += 1
                else:
                    print(f"Test {i + 1} failed: Output mismatch")
                    print(f"Expected: {expected_lines}")
                    print(f"Actual: {output_lines}")
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
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print(f"\n--- Test Summary ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    return {"passed": passed_tests, "total": total_tests}

tasks = load_apps_tests(test_data_path)

if tasks:
    results = {}
    temp_dir = "tempfolder"
    os.makedirs(temp_dir, exist_ok=True)

    for folder_name, folder_path in folder_paths.items():
        print(f"\n--- Running {folder_name} Tests ---")
        results[folder_name] = run_tests_on_code_snippets(tasks, folder_path, temp_dir)

    print("\n--- Overall Test Summary ---")
    for folder, result in results.items():
        print(f"{folder}: Passed {result['passed']} of {result['total']}")

    total_passed = sum(result['passed'] for result in results.values())
    total_all = sum(result['total'] for result in results.values())
    print(f"\nTotal Passed: {total_passed} of {total_all}")

    shutil.rmtree(temp_dir)