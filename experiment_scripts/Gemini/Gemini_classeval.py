import base64
import os
from google import genai
from google.genai import types
import json
import sys

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) # access content in main folder
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # access content from one step up in folders
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

    model = "gemini-2.0-flash" 
    system_prompt = prompt.SYSTEM_PROMPT #or some other system prompt.
    user_prompt = system_prompt + prompt.HEAD_PROMPT + task_prompt + prompt.TAIL_PROMPT

    contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_prompt)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,
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

    # Extract and return the assistant's reply
    return response.text


def load_classEval_tasks(json_file_path):
    """Loads class evaluation tasks from a JSON file."""
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                tasks.append(item["skeleton"]) # Assumes each item in the JSON list has a 'skeleton' key
        return tasks
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None

if __name__ == "__main__":
    # Load tasks from the ClassEval CSV file
    csv_file_path = os.path.join(main_dir, "data", "ClassEval_data.json")
    tasks = load_classEval_tasks(csv_file_path)

    if tasks is None:
        sys.exit(1) 

    # Define the index interval for tasks
    start_index = 0
    end_index = 40

    results = []
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")
        assistant_response = run_task_with_gemini(task_prompt)
        results.append({"task_index": i, "assistant_response": assistant_response})

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "Gemini", "classEval", prompt.PROMPT_TECHNIQUE_SETTING)
    json_file_path = os.path.join(results_dir, "classeval_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)

