import base64
import os
from google import genai
from google.genai import types
import csv
import json
import sys

thesis_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(thesis_dir)

import config
from extract_code_python import extract_and_save_python_code

def run_task_with_gemini(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the Gemini API.
    """
    client = genai.Client(api_key=config.GEMINI_API_KEY)

    model = "gemini-2.0-flash" # or gemini-2.0-flash, or gemini-ultra if you have access.
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=task_prompt + " Give only the code.")],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,
        top_p=1,
        top_k=40,
        max_output_tokens=800,
        response_mime_type="text/plain",
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Extract and return the assistant's reply
    return response.text


def load_cli_games_tasks(csv_file_path):
    instructions = []
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instructions.append(row["prompt"])
        return instructions
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_results_to_json(results, output_file):
    output_data = {}
    for entry in results:
        output_data[entry["task_index"]] = entry["assistant_response"]

    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile, ensure_ascii=False, indent=4) #ensure_ascii=False ensures non-ascii characters are correctly saved.
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Load all tasks from the CSV file
    csv_file_path = os.path.join("data", "cli_games.csv")
    tasks = load_cli_games_tasks(csv_file_path)

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

    json_file_path = 'test_cli_games.json'
    # Save all results to a json file
    save_results_to_json(results, json_file_path)

    output_directory = 'results/Gemini/cli_games'
    extract_and_save_python_code(json_file_path, output_directory)