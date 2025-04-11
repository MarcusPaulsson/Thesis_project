import os
import sys
import json
from llama_cpp import Llama
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

def load_llama_model(model_path, ctx_window=8000, n_gpu_layers=-1, verbose=True):
    """
    Loads the Llama model and returns the Llama instance with CUDA enabled.
    Prints information about layer offloading to verify GPU usage.
    """
    llm = Llama(model_path=model_path, n_ctx=ctx_window, n_gpu_layers=n_gpu_layers, n_threads=os.cpu_count(), verbose=verbose)
    return llm

def run_task_with_llama(llm, task_prompt, temp=0.2):
    """
    Run a single task using the provided Llama instance, passing the task prompt.
    """
    output = llm(
        task_prompt,
        temperature=temp,
        top_k=1,
        max_tokens=2500,  # -1 means no limit
        stream=True,
        echo=False,  # do not echo the prompt.
    )

    full_response = ""
    for part in output:
        content = part['choices'][0]['text']
        full_response += content
        print(content, end='', flush=sys.stdout)  # Print to stdout for streaming

    return full_response


def extract_apps_tasks(json_file_path):
    """
    Extracts 'question' and 'test' fields from each line in a JSON file.
    """
    tasks = []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            for line in jsonfile:
                line = line.strip()
                try:
                    data = json.loads(line)
                    if "question" in data and "input_output" in data:
                        current_task = data["question"]
                        extra_prompt = "\n Here is some of the test cases: " 
                        test_cases =  data["input_output"]
                        temp = json.loads(test_cases)
                        max_numb_test = 5
                        list_of_input = temp["inputs"][:max_numb_test]
                        list_of_outputs = temp["outputs"][:max_numb_test]
                        test_string = "inputs:\n"
                        test_string = extra_prompt + test_string
                        for i in range(len(list_of_input)):
                            test_string += list_of_input[i]
                        test_string += "  Outputs:\n"
                        for i in range(len(list_of_input)):
                            test_string += list_of_outputs[i]
                        tasks.append(current_task + test_string)
                  
                    elif "question" in data:
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

if __name__ == "__main__":
    # Load tasks from the APPS JSON file
    apps_file_path = os.path.join(main_dir, "data", "apps.json")  # Adjust filename and path
    tasks = extract_apps_tasks(apps_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 20
    end_index = 30  # Adjust to the number of tasks you want to run.

    results = {}  # Change results to a dictionary
    skip_test = [4, 21, 37, 43, 48, 65, 85, 98]
    # Load the Llama model once with CUDA
    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "Qwen2.5-Coder-14B-Instruct-128K-GGUF"))
    model_path = os.path.join(model_dir, "Qwen2.5-Coder-14B-Instruct-Q5_K_M.gguf")
    llm = load_llama_model(model_path)

    for i in range(start_index, end_index): # Stream run
        pass
    for i in skip_test:                      # specific run
        task_prompt = tasks[i]
        print(f"Processing task {i}...")

        # Construct the prompt according to Qwen's chat template
        prompt_parts = [
            f"<|im_start|>system\n{prompt.SYSTEM_PROMPT}<|im_end|>\n",
            f"<|im_start|>user\n{prompt.HEAD_PROMPT}{task_prompt}{prompt.TAIL_PROMPT}<|im_end|>\n",
            "<|im_start|>assistant\n"  # Prepare for assistant's response
        ]
        user_prompt = "".join(prompt_parts)

        # Run the task with the Qwen LLM (replace with your actual LLM call)
        assistant_response = run_task_with_llama(llm, user_prompt)  # Replace this!

        results[str(i)] = assistant_response  # Use task index as key

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "Qwen", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)