import os
import sys
import json
from llama_cpp import Llama

# Adjust paths as needed
upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)

from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt

def run_task_with_llama(task_prompt, model_path):
    """
    Run a single task using Llama, passing the task prompt as the user's message.
    """
    llm = Llama(model_path=model_path)

    output = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": task_prompt
            }
        ],
        temperature=0.7,
        top_p=0.1,
    )

    return output['choices'][0]['message']['content']

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

if __name__ == "__main__":
    # Adjust paths as needed
    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "DeepSeek-R1-Distill-Qwen-7B-GGUF"))
    model_path = os.path.join(model_dir, "DeepSeek-R1-Distill-Qwen-7B-Q3_K_L.gguf")
    apps_file_path = os.path.join(main_dir, "data", "apps.json")  # Adjust filename and path

    tasks = "Give me an implementation of bubblesort using python"

    if tasks is None:
        sys.exit(1)

    start_index = 0
    end_index = 1  # Adjust to the number of tasks you want to run.

    results = []
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        task_prompt += " Use python for coding."
        print(f"Processing task {i}...")
        assistant_response = run_task_with_llama(task_prompt, model_path)
        results.append({"task_index": i, "assistant_response": assistant_response})

    results_dir = os.path.join(main_dir, "results", "LlamaCPP", "APPS", "DeepSeek-R1-Distill-Qwen-7B")  # Adjust directory as needed.
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "apps_raw.json")
    save_results_to_json(results, json_file_path)
    print(f"Results saved to {json_file_path}")