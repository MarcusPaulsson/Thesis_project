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

def load_llama_model(model_path, ctx_window=16384, n_gpu_layers=-1, verbose=True):
    """
    Loads the Llama model and returns the Llama instance with CUDA enabled.
    Prints information about layer offloading to verify GPU usage.
    """
    llm = Llama(model_path=model_path, n_ctx=ctx_window, n_gpu_layers=n_gpu_layers, n_threads=os.cpu_count(), verbose=verbose)
    return llm

def run_task_with_llama(llm, task_prompt, temp=0.7):
    """
    Run a single task using the provided Llama instance, passing the task prompt.
    """
    output = llm(
        task_prompt,
        temperature=temp,
        max_tokens=-1,  # -1 means no limit
        stream=True,
        echo=False,  # do not echo the prompt.
    )

    full_response = ""
    for part in output:
        content = part['choices'][0]['text']
        full_response += content
        print(content, end='', flush=sys.stdout)  # Print to stdout for streaming

    return full_response

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
    

# def extract_apps_tasks(json_file_path):
#     """
#     Extracts 'question' fields from each line in a JSON file, handling potential errors.
#     """
#     tasks = []
#     try:
#         with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
#             for line in jsonfile:
#                 line = line.strip()
                
#                 try:
#                     data = json.loads(line)
#                     if "question" in data:
#                         tasks.append(data["question"])
#                 except json.JSONDecodeError:
#                     print(f"Warning: Skipping invalid JSON line: {line[:50]}...")
#         return tasks
#     except FileNotFoundError:
#         print(f"Error: JSON file '{json_file_path}' not found.")
#         return None

def save_results_to_json(results, json_file_path):
    """
    Saves results to a JSON file.
    """
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Load tasks from the APPS JSON file
    apps_file_path = os.path.join(main_dir, "data", "ultra_simple.json")
    tasks = load_cli_games_tasks_from_json(apps_file_path)

    if tasks is None:
        sys.exit(1)

    # Define the index interval for tasks
    start_index = 0
    end_index = 3  # Adjust to the number of tasks you want to run.

    results = {}  # Change results to a dictionary

    # Load the Llama model once with CUDA
    model_dir = os.path.abspath(os.path.join(upper_main_dir, "Models", "WizardCoder-15B-V1.0-GGUF"))
    model_path = os.path.join(model_dir, "WizardCoder-15B-V1.0.Q4_K_S.gguf")
    llm = load_llama_model(model_path)

    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        task_prompt = '''
Polycarp has a set of n distinct binary words (each word consists solely of the characters '0' and '1'). He wants to use these words in a game where:
- The first word can be any word.
- Every subsequent word must start with the last character of the previous word.
Words can be reversed (i.e., their characters are in reverse order) to help form such a sequence, but after any reversals the words must remain distinct. Polycarp's goal is to reverse the minimum number of words so that the entire set can be arranged to follow the game's rule. If no valid arrangement exists even after reversals, the answer is -1.
Input Format:
- The first line contains an integer t (1 <= t <= 10^4) - the number of test cases.
- For each test case:
  - The first line contains an integer n (1 <= n <= 2x10^5) - the number of words.
  - The next n lines each contain a non-empty binary word (each word consists only of '0' and '1').
    The sum of the lengths of all words in all test cases is at most 4x10^6.
    All words in a test case are distinct.
Output Format:
- For each test case, output:
  - -1 if no valid ordering exists.
  - Otherwise, output two lines:
    - The first line contains k (0 <= k <= n) - the minimal number of words to reverse.
    - The second line contains k distinct integers (indices from 1 to n) indicating which words to reverse.
      (If k = 0, the second line may be omitted or left empty.)

Example:

Input
4
4
0001
1000
0011
0111
3
010
101
0
2
00000
00001
4
01
001
0001
00001

Output
1
3
-1
0
2
1 2
 '''
        print(task_prompt)
        print(f"Processing task {i}...")
        system_prompt = prompt.SYSTEM_PROMPT  # or some other system prompt.
        user_prompt = system_prompt + prompt.HEAD_PROMPT + task_prompt + prompt.TAIL_PROMPT
        assistant_response = run_task_with_llama(llm, user_prompt)  # Pass the loaded llm instance
        results[str(i)] = assistant_response  # Use task index as key

    # Save results to JSON and extract Python code
    results_dir = os.path.join(main_dir, "results", "WizardCoder", "cli_games", prompt.PROMPT_TECHNIQUE_SETTING)
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
    json_file_path = os.path.join(results_dir, "cli_games_raw.json")
    save_results_to_json(results, json_file_path)
    extract_and_save_python_code(json_file_path, results_dir)