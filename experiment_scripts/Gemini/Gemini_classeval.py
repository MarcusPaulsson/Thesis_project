import base64
import os
from google import genai
from google.genai import types
import json
import sys
import time 
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) # access content in main folder
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # access content from one step up in folders
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
    model = "gemini-2.0-flash"
    user_prompt = system_prompt + " Use python to code. \n\n" + task_prompt + + prompt.TAIL_PROMPT
  
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

def load_classEval_tasks(json_file_path):
    """Loads class evaluation tasks from a JSON file."""
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                text = item["skeleton"]
                test_cases = " Here is the test cases the code shall pass: " + item['test']
                tasks.append(text +test_cases) # Assumes each item in the JSON list has a 'skeleton' key

        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None

if __name__ == "__main__":
    # Load tasks from the ClassEval JSON file
    classeval_file_path = os.path.join(main_dir, "data", "ClassEval_data.json")
    tasks = load_classEval_tasks(classeval_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 0
    end_index = 100
    run_iterative = True if (prompt.PROMPT_TECHNIQUE_SETTING == "Iterative" or prompt.PROMPT_TECHNIQUE_SETTING == "Combined") else False
    results = []

    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")
        if run_iterative:
            api_result = process_task_with_iterations(task_prompt)
            if api_result and api_result.get("assistant_response"):
                results.append({"task_index": i, "assistant_response": api_result["assistant_response"]})
            elif api_result and api_result.get("error"):
                print(f"Task {i} failed: {api_result['error']}")
            else:
                print(f"Task {i} encountered an unexpected issue during iterations.")
        else:
            assistant_response = run_task_with_gemini_iter(task_prompt, prompt.SYSTEM_PROMPT)
            if assistant_response:
                results.append({"task_index": i, "assistant_response": assistant_response})
            else:
                print(f"Task {i} failed during the first iteration.")

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "Gemini_test2", "classEval", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)
    json_file_path = os.path.join(results_dir, "classeval_raw.json")

    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)