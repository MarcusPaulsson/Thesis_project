import json
from openai import OpenAI
import sys
import os

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) # access content in main folder
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # access content from one step up in folders
sys.path.append(main_dir)
sys.path.append(upper_dir)

import config
from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt


def run_task_with_api(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the OpenAI API.
    """
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        
        messages = [
    {"role": "system", "content": prompt.SYSTEM_PROMPT},
    {"role": "user", "content": prompt.TAIL_PROMPT+task_prompt+prompt.TAIL_PROMPT}
],
        response_format={"type": "text"},
        temperature=0.7,
        max_completion_tokens=1400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
   
    # Extract and return the assistant's reply
    return response.choices[0].message.content


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
    

if __name__ == "__main__":
    # Load all tasks from the CSV file
    tasks = "Give me a full implementation of the game battleship with a command line interface."
    json_file_path = os.path.join("data", "cli_games.json")
    tasks = load_cli_games_tasks_from_json(json_file_path)


    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # change as needed
    end_index = 18   # change as needed
    
    results = []  # Dictionary to hold responses for each task
    
    # Loop through the selected task indices in the main method
    for i in range(start_index, end_index):
        task_prompt = tasks[i] 
        print(f"Processing task {i}...")
        
        # Call the API for this task prompt
        assistant_response = run_task_with_api(task_prompt)
        
        # Save the result in the results list
        results.append({
            "task_index": i,
            "assistant_response": assistant_response
        })
    
    json_file_path = 'results/ChatGPT/cli_games/cli_games_raw.json'  # Replace with your JSON file path
    # Save all results to a CSV file
    save_results_to_json(results, json_file_path)

    output_directory = 'results/ChatGPT/cli_games' #where the python files will be saved.
    extract_and_save_python_code(json_file_path,output_directory)

