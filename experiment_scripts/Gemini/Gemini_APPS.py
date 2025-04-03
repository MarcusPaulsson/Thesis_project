import base64
import os
from google import genai
from google.genai import types
import json
import sys
import re

# Adjust paths as needed
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

import config
from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def run_task_with_gemini(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the Gemini API.
    """
    client = genai.Client(api_key=config.GEMINI_API_KEY)

    model = "gemini-2.0-flash"  # or "gemini-pro", "gemini-2.0-pro"
    system_prompt = prompt.SYSTEM_PROMPT  # or some other system prompt.
    user_prompt = system_prompt + prompt.HEAD_PROMPT + task_prompt + prompt.TAIL_PROMPT

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_prompt)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,  # Adjust as needed
        top_p=1,
        top_k=40,
        max_output_tokens=2500,  # Adjust as needed
        response_mime_type="text/plain",
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Extract and return the assistant's reply
    return response.text

def extract_apps_tasks(json_file_path):
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            try:
                # Load the entire JSON array at once
                data_array = json.load(jsonfile)
                
                # Process each item in the array
                for item in data_array:
                    if "question" in item:
                        tasks.append(item["question"])
                    else:
                        print(f"Warning: Skipping item with missing 'question' field: {str(item)[:50]}...")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
                
        print(f"Successfully extracted {len(tasks)} questions from {json_file_path}")
        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None

if __name__ == "__main__":
    # Load tasks from the APPS JSON file
    apps_file_path = os.path.join(main_dir, "data", "apps.json")  # Adjust filename and path
    tasks = extract_apps_tasks(apps_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 0
    end_index = 49  # Adjust to the number of tasks you want to run.

    results = []
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        task_prompt + " Use python for coding."
        print(f"Processing task {i}...")
        assistant_response = run_task_with_gemini(task_prompt)
        results.append({"task_index": i, "assistant_response": assistant_response})

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "Gemini", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)  # Adjust directory as needed.
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)
