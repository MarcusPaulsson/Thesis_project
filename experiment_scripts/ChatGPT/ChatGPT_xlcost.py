import json
from openai import OpenAI
import sys
import os
import csv

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
    {"role": "user", "content": task_prompt+ prompt.TAIL_PROMPT}
],
        response_format={"type": "text"},
        temperature=0.2,
        max_completion_tokens=2500,
        top_p=1,
    )
   
    # Extract and return the assistant's reply
    return response.choices[0].message.content


def extract_descriptions_from_csv(csv_file_path):
    """
    Extracts the text descriptions from a CSV file structured as "text,code".
    Returns a list of the text descriptions.
    """
    descriptions = []
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row (if it exists)
            for row in reader:
                if row:  # Ensure the row is not empty
                    description = row[0].strip()  # Extract the first element (text) and remove leading/trailing whitespace
                    descriptions.append(description)
        return descriptions
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Load all tasks from the CSV file
    tasks = "Give me a full implementation of the game battleship with a command line interface."
    json_file_path = os.path.join(main_dir,"data", "xlcost-t2c-python.csv")
    tasks = extract_descriptions_from_csv(json_file_path)


    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # change as needed
    end_index = 10   # change as needed
    
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

    
    results_dir = os.path.join(main_dir, "results", "ChatGPT", "xlcost", prompt.PROMPT_TECHNIQUE_SETTING)
    json_file_path = os.path.join(results_dir, "xlcost.json")
    os.makedirs(results_dir, exist_ok=True)
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)


