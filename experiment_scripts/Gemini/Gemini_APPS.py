import base64
import os
from google import genai
from google.genai import types
import json
import sys
import re
import time
import concurrent.futures

# Adjust paths as needed
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

import config
from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def run_task_with_gemini_iter(task_prompt, system_prompt):
    """
    Runs a single iteration of a task using the Gemini API.
    """
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    model = "gemini-2.0-flash"  # or "gemini-pro", "gemini-2.0-pro"
    user_prompt = system_prompt + " Use python to code. \n\n" + task_prompt + prompt.TAIL_PROMPT

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_prompt)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        top_p=1,
        top_k=40,
        max_output_tokens=2500,
        response_mime_type="text/plain",
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text

def process_task_with_iterations(task_prompt):
    """Runs a single task through multiple iterations."""
    print(f"Processing task with iterations...")
    result_iter1 = run_task_with_gemini_iter(task_prompt, prompt.SYSTEM_PROMPT[0])
    if not result_iter1:
        return {"assistant_response": None, "error": "Iteration 1 failed"}
    assistant_response_iter1 = result_iter1
    result_iter2 = run_task_with_gemini_iter(assistant_response_iter1 + "\n" + task_prompt, prompt.SYSTEM_PROMPT[1])
    if not result_iter2:
        return {"assistant_response": None, "error": "Iteration 2 failed"}
    return {"assistant_response": result_iter2, "error": None}

def extract_apps_tasks(json_file_path):
    """
    Extracts 'question' and 'test' fields from each line in a JSON file.
    """
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            for line in jsonfile:
                line = line.strip()
                try:
                    data = json.loads(line)
                    if "question" in data and "input_output" in data:
                        current_task = data["question"]
                        extra_prompt = "\n Here is some of the test cases: " 
                        test_cases =  data["input_output"]
                        temp = json.loads(test_cases)
                        max_numb_test = 5
                        list_of_input = temp["inputs"][:max_numb_test]
                        list_of_outputs = temp["outputs"][:max_numb_test]
                        test_string = "inputs:\n"
                        test_string = extra_prompt + test_string
                        for i in range(len(list_of_input)):
                            test_string += list_of_input[i]
                        test_string += "  Outputs:\n"
                        for i in range(len(list_of_input)):
                            test_string += list_of_outputs[i]
                        tasks.append(current_task + test_string)
                  
                    elif "question" in data:
                        tasks.append(data["question"])
                except json.JSONDecodeError:
                    print(f"Warning: Skipping invalid JSON line: {line[:50]}...")
        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None

def process_tasks_parallel(tasks, start_index, end_index, max_workers=5, iterative=False):
    """Processes tasks in parallel using ThreadPoolExecutor, with optional iteration."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for i in range(start_index, min(end_index, len(tasks))):
            if i in skip_test:
                continue
            else:
                task_prompt = tasks[i]
                if iterative:
                    future = executor.submit(process_task_with_iterations, task_prompt)
                else:
                    future = executor.submit(run_task_with_gemini_iter, task_prompt, prompt.SYSTEM_PROMPT) # Run only first prompt if not iterative
                futures[future] = i

        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            api_result = future.result()
            if iterative:
                if api_result and api_result.get("assistant_response"):
                    results.append({"task_index": index, "assistant_response": api_result["assistant_response"]})
                elif api_result and api_result.get("error"):
                    print(f"Task {index} failed: {api_result['error']}")
                else:
                    print(f"Task {index} encountered an unexpected issue during iterations.")
            else:
                if api_result:
                    results.append({"task_index": index, "assistant_response": api_result})
                else:
                    print(f"Task {index} failed during the first iteration.")
    return results

if __name__ == "__main__":
    # Load tasks from the APPS JSON file
    apps_file_path = os.path.join(main_dir, "data", "apps.json")  # Adjust filename and path
    tasks = extract_apps_tasks(apps_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 0
    end_index = 100  # Adjust to the number of tasks you want to run.
    max_workers = 1 # Adjust the number of parallel threads
    run_iterative = True if (prompt.PROMPT_TECHNIQUE_SETTING == "Iterative" or prompt.PROMPT_TECHNIQUE_SETTING == "Combined") else False
    skip_test = [4, 21, 26, 37, 43, 48, 61, 65, 75, 85, 98]
    skip_test = []
    results = process_tasks_parallel(tasks, start_index, end_index, max_workers, run_iterative)

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "Gemini", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)  # Adjust directory as needed.
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)