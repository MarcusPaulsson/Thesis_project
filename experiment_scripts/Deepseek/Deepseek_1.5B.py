import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import sys



upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_main_dir)
sys.path.append(main_dir)
sys.path.append(upper_dir)


from extract_code_python import extract_and_save_python_code, save_results_to_json

def load_cli_games_tasks_from_json(json_file_path):
    """Load game instructions from a JSON file."""
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

def run_task_with_local_model(task_prompt, tokenizer, model, device):
    """Runs the local DeepSeek model on a given prompt."""
    extra_message = "Give only the code."
    formatted_prompt = f"{task_prompt} {extra_message}"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)

    start_time = time.time()

    with torch.inference_mode(), torch.amp.autocast("cuda" if device.type == "cuda" else "cpu"):
        output_ids = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=5000,
            temperature=0.7,
            top_k=40,
            top_p=1,
        )

    elapsed_time = time.time() - start_time
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return generated_text, elapsed_time

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model_name_or_path = os.path.join(upper_main_dir, "Models/DeepSeek-R1-Distill-Qwen-1.5B")

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, local_files_only=True)

    with torch.inference_mode():
        model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            local_files_only=True
        ).to(device)

    json_file_path = os.path.join(main_dir, "data", "cli_games.json")
    tasks = load_cli_games_tasks_from_json(json_file_path)

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
            "execution_time": execution_time
        })

    results_dir = os.path.join(main_dir, "results", "Deepseek", "cli_games", "Zero-shot") # added default prompt to make it match the other script.
    os.makedirs(results_dir, exist_ok=True) # create result directory if it does not exist.
    json_file_path = os.path.join(results_dir, "cli_games_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)