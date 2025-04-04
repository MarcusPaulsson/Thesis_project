import json
from openai import OpenAI
import sys
import os
import concurrent.futures

# Adjust paths to access config.py and extract_code_python.py
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)
import config

from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def extract_apps_tasks(json_file_path):
    """
    Extracts 'question' fields from each line in a JSON file, handling potential errors.
    """
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            for line in jsonfile:
                line = line.strip()
                try:
                    data = json.loads(line)
                    if "question" in data:
                        tasks.append(data["question"])
                except json.JSONDecodeError:
                    print(f"Warning: Skipping invalid JSON line: {line[:50]}...")
        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None

def run_task_with_api(task_prompt):
    """Runs a single task using the OpenAI API."""
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    extra_message = " Use python to code. Give only the code."
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt.SYSTEM_PROMPT},
                {"role": "user", "content": task_prompt + extra_message}
            ],
            response_format={"type": "text"},
            temperature=0.7,
            max_completion_tokens=2500,
            top_p=1,
        )
        total_tokens = response.usage.total_tokens
        print(f"Task processed, Token count: {total_tokens}")
        return {"response": response.choices[0].message.content, "error": None}
    except Exception as e:
        print(f"Error processing task: {e}")
        return {"response": None, "error": str(e)}

def process_tasks_parallel(tasks, start_index, end_index, max_workers=5):
    """Processes tasks in parallel using ThreadPoolExecutor."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_task_with_api, tasks[i]): i for i in range(start_index, min(end_index, len(tasks)))}
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            api_result = future.result()
            if api_result["response"]:
                results.append({"task_index": index, "assistant_response": api_result["response"]})
            else:
                print(f"Task {index} failed: {api_result['error']}")
    return results

if __name__ == "__main__":
    # Load tasks from the APPS JSON file
    apps_file_path = os.path.join(main_dir, "data", "apps.json")
    tasks = extract_apps_tasks(apps_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 0
    end_index = 100  # Adjust to the number of tasks you want to run.
    max_workers = 10 # Adjust the number of parallel threads

    results = process_tasks_parallel(tasks, start_index, end_index, max_workers)

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "ChatGPT", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)