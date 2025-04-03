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

def load_ctransformers_model(model_repo, model_file, model_type="llama", gpu_layers=30, context_length=2048):
    """Loads a model using ctransformers."""
    llm = AutoModelForCausalLM.from_pretrained(
        model_repo,
        model_file=model_file,
        model_type=model_type,
        gpu_layers=gpu_layers,
        context_length=context_length
    )
    return llm


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


def run_task_with_ctransformers(llm, task_prompt, temp=0.7):
    """Run a single task using ctransformers."""
    output = llm(
        task_prompt,
        temperature=temp,
        max_new_tokens=4096,  # Adjust as needed
        stream=True,
    )

    full_response = ""
    for part in output:
        content = part
        full_response += content
        print(content, end='', flush=sys.stdout)

    return full_response


def save_results_to_json(results, json_file_path):
    """
    Saves results to a JSON file.
    """
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    apps_file_path = os.path.join(main_dir, "data", "apps.json")
    tasks = extract_apps_tasks(apps_file_path)

    if tasks is None:
        sys.exit(1)

    start_index = 17
    end_index = 30

    results = {}

    # Load the model using ctransformers
    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "WizardCoder-Python-13B-V1.0-GGUF"))
    model_path = os.path.join(model_dir, "wizardcoder-python-13b-v1.0.Q5_K_S.gguf")
    llm = load_ctransformers_model(model_dir, model_path)


    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")
        # Construct the prompt according to WizardCoder's template
        user_prompt = f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt.SYSTEM_PROMPT}{task_prompt}{prompt.TAIL_PROMPT}\n\n### Response:"
        # Run the task with the WizardCoder LLM (ctransformers)
        assistant_response = run_task_with_ctransformers(llm, user_prompt)

        results[str(i)] = assistant_response

    results_dir = os.path.join(main_dir, "results", "WizardCoder", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)