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
    system_prompt = prompt.SYSTEM_PROMPT_SENIOR #or some other system prompt.
    user_prompt = system_prompt + "\n" + task_prompt + " Give only the code."

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
        max_output_tokens=1400,
        response_mime_type="text/plain",
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Extract and return the assistant's reply
    return response.text


def load_cli_games_tasks_from_json(json_file_path):
    """
    Load game instructions from a JSON file.
    Assumes the JSON file contains a list of dictionaries, where each dictionary
    has a 'prompt' key.
    Returns a list of game instruction prompts.
    """
    instructions = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                instructions.append(item["prompt"])
        return instructions
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Load all tasks from the JSON file
    json_file_path = os.path.join("data", "cli_games.json")
    tasks = load_cli_games_tasks_from_json(json_file_path)

    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0
    end_index = 18

    results = []

    # Loop through the selected task indices in the main method
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")

        # Call the API for this task prompt
        assistant_response = run_task_with_gemini(task_prompt)

        # Save the result in the results list
        results.append({
            "task_index": i,
            "assistant_response": assistant_response
        })

    json_file_path = 'results/Gemini/cli_games/cli_games_raw.json'
    # Save all results to a JSON file
    save_results_to_json(results, json_file_path)

    output_directory = 'results/Gemini/cli_games'
    extract_and_save_python_code(json_file_path, output_directory)