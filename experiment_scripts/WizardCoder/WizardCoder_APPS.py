import time
import os
import torch
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from accelerate import Accelerator

import json
upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_main_dir)
sys.path.append(main_dir)
sys.path.append(upper_dir)

from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt
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



def run_task_with_local_model(task_prompt, tokenizer, model, device):
    """Runs the local model on a given prompt with streaming."""
    

    system_prompt = prompt.SYSTEM_PROMPT  # or some other system prompt.
    user_prompt = system_prompt + prompt.HEAD_PROMPT + task_prompt + prompt.TAIL_PROMPT
    formatted_prompt = f"{user_prompt}"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)
    
    start_time = time.time()

    streamer = TextStreamer(tokenizer, skip_prompt=True)

    

    with torch.inference_mode(), torch.amp.autocast("cuda" if device.type == "cuda" else "cpu"):
        output_ids = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=5000,
            do_sample=True,
            temperature=0.7,
            top_k=40,
            top_p=1,
            streamer=streamer,
        )
        
    generated_text = tokenizer.decode(output_ids[0])
    elapsed_time = time.time() - start_time

    return generated_text, elapsed_time

if __name__ == "__main__":
    device = torch.device("cuda:0") #set the device directly.
    print(f"Using device: {device}")
    model_name_or_path = os.path.join(upper_main_dir, "Models/WizardCoder-Python-7B-V1.0")

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, local_files_only=True)

    with torch.inference_mode():
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch.bfloat16,
            local_files_only=True,
            device_map="cuda:0" #load directly to gpu.
        )

    json_file_path = os.path.join(main_dir, "data", "apps.json")
    tasks = extract_apps_tasks(json_file_path)
    start_index = 0
    end_index = 1

    results = []
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")
        assistant_response, execution_time = run_task_with_local_model(task_prompt, tokenizer, model, device)
        results.append({
            "task_index": i,
            "assistant_response": assistant_response,
            "execution_time": execution_time,
        })

    results_dir = os.path.join(main_dir, "results", "WizardCoder", "APPS", "Zero-shot")
    os.makedirs(results_dir, exist_ok=True)
    json_file_path = os.path.join(results_dir, "cli_games_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)