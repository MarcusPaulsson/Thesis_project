import os
import json
import subprocess
import sys
import tempfile
import shutil

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)

# Define folder paths in a dictionary
folder_paths = {
    "Gemini Zero-shot": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot')),
    "Gemini Zero-shot-CoT": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot-CoT')),
    "Gemini Student-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Student-role')),
    "Gemini Expert-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Expert-role')),
    "ChatGPT Zero-shot": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot')),
    "ChatGPT Zero-shot-CoT": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot-CoT')),
    "ChatGPT Student-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Student-role')),
    "ChatGPT Expert-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Expert-role')),
    "ChatGPT Meta": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Meta')),
    "ChatGPT Naive": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Naive')),
}

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
        return {"passed": 0, "total": 0, "passed_ids": []}

    passed_tests = 0
    total_tests = len(tasks)
    passed_ids = []
    for i, task in enumerate(tasks):
       
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
                    passed_ids.append(i) # Use i as ID
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
    return {"passed": passed_tests, "total": total_tests, "passed_ids": passed_ids}

tasks = load_classEval_tests(test_data_path)

# Run tests for each folder and store results
if tasks:
    results = {}
    temp_dir = "tempfolder"
    os.makedirs(temp_dir, exist_ok=True)  # creates the temp folder

    for folder_name, folder_path in folder_paths.items():
        print(f"\n--- Running {folder_name} Tests ---")
        results[folder_name] = run_tests_on_code_snippets(tasks, folder_path, temp_dir)

    # Print overall summary
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
    print(f"\nPassed in all folders: {sorted(passed_in_all)}")

    # Cleanup temp folder
    shutil.rmtree(temp_dir)