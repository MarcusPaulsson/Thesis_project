import os
import sys
import json
from ctransformers import AutoModelForCausalLM  # Import ctransformers
import time
import argparse

# Adjust paths as needed
upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def load_ctransformers_model(model_repo, model_file, gpu_layers=45, context_length=2048):
    """Loads a model using ctransformers."""
    llm = AutoModelForCausalLM.from_pretrained(
        model_repo,
        model_file=model_file,
        gpu_layers=gpu_layers,
        context_length=context_length
    )
    return llm

def run_task_with_ctransformers(llm, task_prompt, temp=0.7):
    
    output = llm(
        task_prompt,
        temperature=temp,
        max_new_tokens=1500,  # Adjust as needed
        stream=True,
    )

    full_response = ""
    for part in output:
        content = part
        full_response += content
        print(content, end='', flush=sys.stdout)

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

def save_results_to_json(results, json_file_path):
    """
    Saves results to a JSON file.
    """
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False, indent=4)

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
    apps_file_path = os.path.join(main_dir, "data", "cli_games.json")
    tasks = load_cli_games_tasks_from_json(apps_file_path)

    if tasks is None:
        sys.exit(1)

    start_index = 0
    end_index = 1

    results = {}

    # Load the model using ctransformers
    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "Yi-Coder-9B-Chat-GGUF"))
    model_path = os.path.join(model_dir, "Yi-Coder-9B-Chat-Q4_K_M.gguf")
    llm = load_ctransformers_model(model_dir, model_path)


    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(task_prompt)
        # Construct the prompt according to the Qwen-like template
        user_prompt = f"<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n{prompt.HEAD_PROMPT}{task_prompt}{prompt.TAIL_PROMPT}<|im_end|>\n<|im_start|>assistant"
        # Run the task with ctransformers
        assistant_response = run_task_with_ctransformers(llm, user_prompt)

        results[str(i)] = assistant_response

    results_dir = os.path.join(main_dir, "results", "WizardCoder", "classEval", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)
    json_file_path = os.path.join(results_dir, "classeval_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)