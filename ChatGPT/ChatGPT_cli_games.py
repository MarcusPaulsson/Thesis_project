import csv
from openai import OpenAI
import json
import sys
import os

thesis_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..'))
sys.path.append(thesis_dir)

import config
from extract_code_python import extract_and_save_python_code 

def run_task_with_api(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the OpenAI API.
    """
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    extra_message = "Give only the code."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        
        messages = [
    #{"role": "system", "content": "You are a beginner level, programming student."},
    {"role": "system", "content": "You are a beginner software engineering student"},
    {"role": "user", "content": task_prompt+extra_message}
],
        response_format={"type": "text"},
        temperature=0.7,
        max_completion_tokens=800,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
   
    # Extract and return the assistant's reply
    return response.choices[0].message.content

import csv
import os 

def load_cli_games_tasks(csv_file_path):
    """
    Load game instructions from a CSV file.
    Assumes the CSV file has a header with columns:
    task_id, prompt
    Returns a list of game instruction prompts (from the "prompt" field).
    """
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
    tasks = "Give me a full implementation of the game battleship with a command line interface."
    csv_file_path = os.path.join("data", "cli_games.csv") #the .. means go up one directory.
    tasks = load_cli_games_tasks(csv_file_path)


    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # change as needed
    end_index = 18    # change as needed
    
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
    
    json_file_path = 'test.json'  # Replace with your JSON file path
    # Save all results to a CSV file
    save_results_to_json(results, json_file_path)

    output_directory = 'results/ChatGPT/cli_games' #where the python files will be saved.
    extract_and_save_python_code(json_file_path,output_directory)

