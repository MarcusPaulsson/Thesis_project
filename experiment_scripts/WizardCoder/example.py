import os
import sys
import json
from llama_cpp import Llama
import time
# Adjust paths as needed
upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def run_task_with_llama(task_prompt):
    """
    Run a single task using Llama, passing the task prompt as the user's message.
    """

    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "WizardCoder-Python-13B-V1.0-GGUF"))
    model_path = os.path.join(model_dir, "wizardcoder-python-13b-v1.0.Q6_K.gguf")
    llm = Llama(model_path=model_path)
    stream = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": task_prompt
            }
        ],
        temperature=0.7,
        top_p=0.1,
        stream=True,  # Enable streaming
        max_tokens=100, # Add max_tokens
    )
    full_response = ""
    for part in stream:
        content = part['choices'][0]['delta'].get('content', '')
        print(content, end='', flush=sys.stdout) #Print each part of the response
        full_response += content
    return full_response

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

def save_results_to_json(results, json_file_path):
    """
    Saves results to a JSON file.
    """
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False, indent=4)

    

if __name__ == "__main__":
      # Load tasks from the APPS JSON file
      apps_file_path = os.path.join(main_dir, "data", "cli_games.json")  # Adjust filename and path
      tasks = load_cli_games_tasks_from_json(apps_file_path)

      if tasks is None:
            sys.exit(1)

      # Define the index interval for tasks
      start_index = 0
      end_index = 1  # Adjust to the number of tasks you want to run.

      results = []
      for i in range(start_index, end_index):
            task_prompt = tasks[i]
            
            print(f"Processing task {i}...")

            assistant_response = run_task_with_llama(task_prompt)
            results.append({"task_index": i, "assistant_response": assistant_response})

      # Save results to JSON and extract Python code
      results_dir = os.path.join(main_dir, "results", "ChatGPT", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)
      os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
      json_file_path = os.path.join(results_dir, "apps_raw.json")
      save_results_to_json(results, json_file_path)
      extract_and_save_python_code(json_file_path, results_dir)