import os
import csv
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set device (GPU if available, else CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define local model path
model_name_or_path = os.path.join(os.getcwd(), "DeepSeek-R1-Distill-Qwen-1.5B")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, local_files_only=True)

# Load model with optimized settings
with torch.inference_mode():  # Enable inference mode for performance
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,  # Use float16 for GPU efficiency
        device_map="auto",
        local_files_only=True
    )

def load_humaneval_tasks(csv_file_path):
    """ Load HumanEval tasks from a CSV file. """
    tasks = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append(row["prompt"])
    return tasks

def run_task_with_local_model(task_prompt):
    """ Runs the local DeepSeek model on a given prompt using PyTorch best practices. """

    # Define system message (acts as context)
    #system_prompt = "You are a senior Python developer. Provide high-quality and optimized code responses."
    
    # Define user task prompt
    extra_message = "Give only the code."

    # Format the final input prompt correctly
    formatted_prompt = f"{task_prompt} {extra_message}"

    # Tokenize input and move to correct device
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)

    # **Start timing before inference**
    start_time = time.time()

    # **Optimized Inference Mode Execution**
    with torch.inference_mode(), torch.amp.autocast("cuda" if device.type == "cuda" else "cpu"):
        output_ids = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=1024,
            do_sample=True,
            temperature=0.2,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.1,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    # **Calculate execution time**
    elapsed_time = time.time() - start_time

    # Decode generated text
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return generated_text, elapsed_time

def save_results_to_csv(results, output_file):
    """ Save model responses to a CSV file. """
    with open(output_file, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["task_index", "assistant_response", "execution_time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in results:
            writer.writerow(entry)

if __name__ == "__main__":
    # Load all tasks from the CSV file
    new_timer = time.time()
    tasks = load_humaneval_tasks("data/humaneval.csv")
    print("Load dataset:",time.time()-new_timer)
    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # Change as needed
    end_index = 2   # Change as needed

    results = []  # List to store responses
    time_0 = time.time()
    # Loop through selected task indices
    for i in range(start_index, end_index):
        task_prompt = tasks[i]

        # Generate response using local model
        assistant_response, timer = run_task_with_local_model(task_prompt)  # Ignore execution_time
        # Store only the assistant's response
        results.append({"assistant_response": assistant_response})
    print(time.time()-time_0)
    # Save all results to a CSV file
    save_results_to_csv(results, "deepseek_responses_expert_humaneval.csv")

    
