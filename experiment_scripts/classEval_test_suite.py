import os
import json
import subprocess
import sys
import tempfile
import shutil
from contextlib import contextmanager
import signal
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)


# Define folder paths in a dictionary
folder_paths = {
    "Gemini Zero-shot": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot')),
    "Gemini Zero-shot-CoT": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Zero-shot-CoT')),
    "Gemini Student-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Student-role')),
    "Gemini Expert-role": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Expert-role')),
    "Gemini Naive": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Naive')),
    "Gemini Iterative": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Iterative')),
    "Gemini Combined": os.path.abspath(os.path.join('results', 'Gemini', 'classEval', 'Combined')),

    "ChatGPT Zero-shot": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot')),
    "ChatGPT Zero-shot-CoT": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Zero-shot-CoT')),
    "ChatGPT Student-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Student-role')),
    "ChatGPT Expert-role": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Expert-role')),
    "ChatGPT Naive": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Naive')),
    "ChatGPT Iterative": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Iterative')),
    "ChatGPT Combined": os.path.abspath(os.path.join('results', 'ChatGPT', 'classEval', 'Combined')),

    "Gemma3 Zero-shot": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Zero-shot')),
    "Gemma3 Zero-shot-CoT": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Zero-shot-CoT')),
    "Gemma3 Student-role": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Student-role')),
    "Gemma3 Expert-role": os.path.abspath(os.path.join('results', 'Gemma3', 'classEval', 'Expert-role')),
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

def count_non_existing_files(verbose_non_existing, folder_paths_list):
    
    for i, item in enumerate(folder_paths_list):
        counter = 0
        for j in range(100):
            filename_to_check = f"code_{j}.py"
            source_file_path = os.path.join(folder_paths_list[item], filename_to_check)
            if not os.path.exists(source_file_path):
                counter+=1
        if verbose_non_existing:
            print(f"Files not exist:{item}  Total: {counter}")


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

def run_single_test(task_index, task, folder_path, global_temp_dir):
    """Runs a single test in a subprocess."""
    file_path = os.path.join(folder_path, f"code_{task_index}.py")
    if not os.path.exists(file_path):
        print(f"Warning: File '{file_path}' not found for test {task_index + 1}.")
        return {"passed": False, "task_index": task_index}

    test_temp_dir = os.path.join(folder_path, f"temp_test_{task_index}")
    os.makedirs(test_temp_dir, exist_ok=True)
    process = None
    passed = False
    stderr_output = ""

    try:
        with open(file_path, 'r') as f:
            generated_code = f.read()

        temp_test_script_path = os.path.join(test_temp_dir, f"run_test_{task_index}.py")
        with open(temp_test_script_path, 'w') as temp_file:
            combined_code = generated_code + "\n\n" + task
            temp_file.write(combined_code + "\nif __name__ == '__main__':\n    import unittest\n    unittest.main()")

        print(f"\n--- Running Test {task_index + 1} in {test_temp_dir} ---")
        process = subprocess.Popen(["python", temp_test_script_path],
                                   cwd=test_temp_dir,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True)
        stdout, stderr = process.communicate(timeout=10) # Increased timeout for parallel runs

        if process.returncode == 0:
            print(f"Test {task_index + 1} passed")
            passed = True
        else:
            print(f"Test {task_index + 1} failed")
            print(f"Stderr:\n{stderr}")
            stderr_output = stderr

    except subprocess.TimeoutExpired:
        print(f"Test {task_index + 1} timed out. Terminating process...")
        if process:
            process.send_signal(signal.SIGTERM)
            time.sleep(1)
            if process.poll() is None:
                process.kill()
    except FileNotFoundError:
        print(f"Error: Python interpreter or file not found for test {task_index + 1}.")
    except Exception as e:
        print(f"Error running test {task_index + 1}: {type(e).__name__} - {e}")
    finally:
        shutil.rmtree(test_temp_dir, ignore_errors=True)
        print(f"Removed temporary directory: {test_temp_dir} (attempted).")

    return {"passed": passed, "task_index": task_index, "stderr": stderr_output}

def run_tests_on_code_snippets_parallel(tasks, folder_path, global_temp_dir, max_workers=12):
    """Runs tests in parallel using ThreadPoolExecutor."""
    if tasks is None:
        return {"passed": 0, "total": 0, "passed_ids": []}

    total_tests = len(tasks)
    passed_tests = 0
    passed_ids = []
    failed_details = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_single_test, i, task, folder_path, global_temp_dir) for i, task in enumerate(tasks)]
        for future in as_completed(futures):
            result = future.result()
            if result and result["passed"]:
                passed_tests += 1
                passed_ids.append(result["task_index"])
            # elif result and not result["passed"] and result["stderr"]:
            #     failed_details[result["task_index"]] = result["stderr"]

    print(f"\n--- Test Summary for {os.path.basename(folder_path)} ---")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    if failed_details:
        print("\n--- Failed Test Details ---")
        for index, error in failed_details.items():
            print(f"Task {index + 1} failed with stderr:\n{error}")

    return {"passed": passed_tests, "total": total_tests, "passed_ids": passed_ids}

tasks = load_classEval_tests(test_data_path)
save_passed = True

# Run tests for each folder in parallel

# Run tests for each folder in parallel
curr_time = time.time()
if tasks:
    results = {}
    with create_and_cleanup_tempdir_global() as global_temp_dir:
        print(f"Using global temporary directory for scripts: {global_temp_dir}")
        for folder_name, folder_path in folder_paths.items():
            print(f"\n--- Running {folder_name} Tests in Parallel ---")
            results[folder_name] = run_tests_on_code_snippets_parallel(tasks, folder_path, global_temp_dir, max_workers=4)

        # Print overall summary and analyze results
        time.sleep(4)
        print(f"Time: {time.time()-curr_time-4}")

        print("\n--- Overall Test Summary ---")
        total_passed = 0
        total_all = len(tasks) * len(folder_paths)
        individual_results = {}
        for folder, result in results.items():
            print(f"{folder}: Passed {result['passed']} of {result['total']}")
            total_passed += result['passed']
            individual_results[folder] = {
                'passed_ids': set(result['passed_ids']),
                'failed_ids': set(range(len(tasks))) - set(result['passed_ids'])
            }

        print("Did not exist:\n")
        print_did_not_exit = True
        count_non_existing_files(print_did_not_exit, folder_paths)

        
        print(f"\nTotal Passed: {total_passed} of {total_all}")

        # Analyze results per model to find IDs that passed all tests
        model_names = sorted(list(set(folder.split()[0] for folder in folder_paths)))
        all_passing_ids = set(range(len(tasks)))  # Start with the assumption all passed
        model_passed_ids = {}
        all_passed_ids = {} # Change to dict for id count
        print("\n--- Analysis of IDs Passing All Tests ---")


        for folder, result in results.items():
            for id in result['passed_ids']:
                if id in all_passed_ids:
                    all_passed_ids[id] += 1
                else:
                    all_passed_ids[id] = 1




        for model in model_names:
            model_folders = [f for f in folder_paths if f.startswith(model)]
            if not model_folders:
                continue

            model_passing_ids = set(range(len(tasks))) # IDs passing for the current model

            print(f"\n--- {model} ---")
            for folder in model_folders:
                passed_in_folder = individual_results[folder]['passed_ids']
                model_passing_ids &= passed_in_folder
                print(f"Passed in {folder}: {sorted(list(passed_in_folder))}")

            print(f"IDs passing all tests for {model}: {sorted(list(model_passing_ids))}")
            if model_names.index(model) == 0:
                all_passing_ids = model_passing_ids.copy()
            else:
                all_passing_ids &= model_passing_ids

        print(f"\n--- Overall IDs Passing All Tests (across all models and techniques) ---")
        print(f"IDs: {sorted(list(all_passing_ids))}")
          
               
        passed_in_all = [id for id, count in all_passed_ids.items() if count == len(folder_paths)]
        common_passed_code = sorted(passed_in_all)
        print(f"\nPassed in all folders: {common_passed_code}")
        if save_passed:
            extract_and_save_passed_code(common_passed_code)
    # The global temporary directory is cleaned up by the context manager