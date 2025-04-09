import os
import json
import subprocess
import sys
import tempfile
import shutil
from contextlib import contextmanager
import signal
import time

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)


# Define folder paths in a dictionary
folder_paths = {
 "Gemini Zero-shot": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot')),
  "Gemini Zero-shot-CoT": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot-CoT')),
  "Gemini Student-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Student-role')),
  "Gemini Expert-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Expert-role')),
  "Gemini Meta": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Meta')),
  "Gemini Naive": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Naive')),
  "Gemini Iterative": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Iterative')),
  "Gemini Combined": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Combined')),

 "ChatGPT Zero-shot": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot')),
 "ChatGPT Zero-shot-CoT": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot-CoT')),
 "ChatGPT Student-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Student-role')),
 "ChatGPT Expert-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Expert-role')),
 "ChatGPT Meta": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Meta')),
  "ChatGPT Naive": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Naive')),
  "ChatGPT Iterative": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Iterative')),
  "ChatGPT Combined": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Combined')),

"Gemma3 Zero-shot": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Zero-shot')),
 "Gemma3 Zero-shot-CoT": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Zero-shot-CoT')),
 "Gemma3 Student-role": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Student-role')),
 "Gemma3 Expert-role": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Expert-role')),
 "Gemma3 Meta": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Meta')),
"Gemma3 Naive": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Naive')),
 "Gemma3 Iterative": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Iterative')),
 "Gemma3 Combined": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Combined')),
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

def extract_and_save_passed_code(passed_code_ids):
    """Extracts and saves passed code snippets to a 'filtered_results' subdirectory."""
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

@contextmanager
def create_and_cleanup_tempdir_global():
    """Context manager for the main temporary directory."""
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Global temporary directory '{temp_dir}' and its contents have been removed (attempted).")

def run_tests_on_code_snippets(tasks, folder_path, global_temp_dir):
    """Runs tests, each within its own temporary subdirectory."""
    if tasks is None:
        return {"passed": 0, "total": 0, "passed_ids": []}

    passed_tests = 0
    total_tests = len(tasks)
    passed_ids = []

    for i, task in enumerate(tasks):
        file_path = os.path.join(folder_path, f"code_{i}.py")

        if os.path.exists(file_path):
            # Create a temporary subdirectory within the current results folder
            test_temp_dir = os.path.join(folder_path, f"temp_test_{i}")
            os.makedirs(test_temp_dir, exist_ok=True)

            try:
                with open(file_path, 'r') as f:
                    generated_code = f.read()

                temp_test_script_path = os.path.join(test_temp_dir, f"run_test_{i}.py")
                with open(temp_test_script_path, 'w') as temp_file:
                    combined_code = generated_code + "\n\n" + task
                    temp_file.write(combined_code + "\nif __name__ == '__main__':\n    import unittest\n    unittest.main()")

                print(f"\n--- Running Test {i + 1} of {total_tests} in {test_temp_dir} ---")
                process = subprocess.Popen(["python", temp_test_script_path],
                                         cwd=test_temp_dir,  # Run from the temporary directory
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         text=True)
                stdout, stderr = process.communicate(timeout=5)

                if process.returncode == 0:
                    print(f"Test {i + 1} passed")
                    passed_tests += 1
                    passed_ids.append(i)
                else:
                    print(f"Test {i + 1} failed")
                    print(f"Stderr:\n{stderr}")

            except subprocess.TimeoutExpired:
                print(f"Test {i + 1} timed out. Terminating process...")
                process.send_signal(signal.SIGTERM)
                time.sleep(1)
                if process.poll() is None:
                    process.kill()
            except FileNotFoundError:
                print(f"Error: Python interpreter or file not found.")
            except Exception as e:
                print(f"Error running test {i + 1}: {type(e).__name__} - {e}")
            finally:
                # Clean up the temporary test directory
                shutil.rmtree(test_temp_dir, ignore_errors=True)
                print(f"Removed temporary directory: {test_temp_dir} (attempted).")
        else:
            print(f"Warning: File '{file_path}' not found for test {i + 1}.")

    print(f"\n--- Test Summary for {os.path.basename(folder_path)} ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    return {"passed": passed_tests, "total": total_tests, "passed_ids": passed_ids}

tasks = load_classEval_tests(test_data_path)
save_passed = True

# Run tests for each folder, using a global temporary directory for temporary scripts
if tasks:
    results = {}
    with create_and_cleanup_tempdir_global() as global_temp_dir:
        print(f"Using global temporary directory for scripts: {global_temp_dir}")
        for folder_name, folder_path in folder_paths.items():
            print(f"\n--- Running {folder_name} Tests ---")
            results[folder_name] = run_tests_on_code_snippets(tasks, folder_path, global_temp_dir)

        # Print overall summary
        print("\n--- Overall Test Summary ---")
        total_passed = 0
        total_all = 0
        all_passed_ids = {}
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

        if save_passed:
            extract_and_save_passed_code(common_passed_code)

    # The global temporary directory is cleaned up by the context manager