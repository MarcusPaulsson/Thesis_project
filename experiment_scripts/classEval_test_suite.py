import os
import json
import subprocess
import sys
import tempfile
import shutil

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)

# Gemini
Gemini_zero_shot_classEval_folder = os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot'))
Gemini_zero_shot_CoT_classEval_folder = os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot-CoT'))
Gemini_student_role_classEval_folder = os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Student-role'))
Gemini_expert_role_classEval_folder = os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Expert-role'))

# ChatGPT
chatGPT_zero_shot_classEval_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot'))
chatGPT_zero_shot_CoT_classEval_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot-CoT'))
chatGPT_student_role_classEval_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Student-role'))
chatGPT_expert_role_classEval_folder = os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Expert-role'))

test_data_path = os.path.abspath(os.path.join('data', 'ClassEval_data.json'))

def load_classEval_tests(test_data_path):
    """Loads class evaluation tasks from a JSON file."""
    tasks = []
    try:
        with open(test_data_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                tasks.append(item["test"])
        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{test_data_path}' not found.")
        return None

def run_tests_on_code_snippets(tasks, folder_path, temp_dir):
    """Runs the tests on the generated code snippets in the specified folder."""
    if tasks is None:
        return {"passed": 0, "total": 0}

    passed_tests = 0
    total_tests = 30
    for i, task in enumerate(tasks):
        if i == 29:
            break
        file_path = os.path.join(folder_path, f"code_{i}.py")

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    generated_code = f.read()

                temp_file_path = os.path.join(temp_dir, f"temp_test_{i}.py")
                with open(temp_file_path, 'w') as temp_file:
                    combined_code = generated_code + "\n\n" + task
                    temp_file.write(combined_code + "\nif __name__ == '__main__':\n    import unittest\n    unittest.main()")

                print(f"\n--- Running Test {i + 1} of {total_tests} ---")
                process = subprocess.run(["python", temp_file_path], capture_output=True, text=True, timeout=10)

                if process.returncode == 0:
                    print(f"Test {i + 1} passed")
                    passed_tests += 1
                else:
                    print(f"Test {i + 1} failed")

            except subprocess.TimeoutExpired:
                print(f"Test {i + 1} timed out.")
            except FileNotFoundError:
                print(f"Error: Python interpreter or file not found.")
            except Exception as e:
                print(f"Error running test {i + 1}: {type(e).__name__} - {e}")
        else:
            print(f"Warning: File '{file_path}' not found for test {i + 1}.")

    print(f"\n--- Test Summary ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    return {"passed": passed_tests, "total": total_tests}

tasks = load_classEval_tests(test_data_path)

# Run tests for each folder and store results
if tasks:
    results = {}
    temp_dir = "tempfolder"
    os.makedirs(temp_dir, exist_ok=True) #creates the temp folder

    # Gemini Tests
    print("\n--- Running Gemini Zero-shot Tests ---")
    results["Gemini Zero-shot"] = run_tests_on_code_snippets(tasks, Gemini_zero_shot_classEval_folder, temp_dir)

    print("\n--- Running Gemini Zero-shot-CoT Tests ---")
    results["Gemini Zero-shot-CoT"] = run_tests_on_code_snippets(tasks, Gemini_zero_shot_CoT_classEval_folder, temp_dir)

    print("\n--- Running Gemini Student-role Tests ---")
    results["Gemini Student-role"] = run_tests_on_code_snippets(tasks, Gemini_student_role_classEval_folder, temp_dir)

    print("\n--- Running Gemini Expert-role Tests ---")
    results["Gemini Expert-role"] = run_tests_on_code_snippets(tasks, Gemini_expert_role_classEval_folder, temp_dir)

    # ChatGPT Tests
    print("\n--- Running ChatGPT Zero-shot Tests ---")
    results["ChatGPT Zero-shot"] = run_tests_on_code_snippets(tasks, chatGPT_zero_shot_classEval_folder, temp_dir)

    print("\n--- Running ChatGPT Zero-shot-CoT Tests ---")
    results["ChatGPT Zero-shot-CoT"] = run_tests_on_code_snippets(tasks, chatGPT_zero_shot_CoT_classEval_folder, temp_dir)

    print("\n--- Running ChatGPT Student-role Tests ---")
    results["ChatGPT Student-role"] = run_tests_on_code_snippets(tasks, chatGPT_student_role_classEval_folder, temp_dir)

    print("\n--- Running ChatGPT Expert-role Tests ---")
    results["ChatGPT Expert-role"] = run_tests_on_code_snippets(tasks, chatGPT_expert_role_classEval_folder, temp_dir)

    # Print overall summary
    print("\n--- Overall Test Summary ---")
    for folder, result in results.items():
        print(f"{folder}: Passed {result['passed']} of {result['total']}")

    total_passed = sum(result['passed'] for result in results.values())
    total_all = sum(result['total'] for result in results.values())
    print(f"\nTotal Passed: {total_passed} of {total_all}")

    #Cleanup temp folder
    shutil.rmtree(temp_dir)