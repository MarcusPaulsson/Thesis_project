import csv
from openai import OpenAI
import config

def load_humaneval_tasks(csv_file_path):
    """
    Load HumanEval tasks from a CSV file.
    Assumes the CSV file has a header with columns:
    task_id, prompt, canonical_solution, test, entry_point
    Returns a list of task descriptions (from the "prompt" field).
    """
    tasks = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append(row["prompt"])
    return tasks

def run_task_with_api(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the OpenAI API.
    """
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    extra_message = "Give only the code."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        
        messages = [
    #{"role": "system", "content": "You are a beginner level, programming student."},
    {"role": "system", "content": "You are a senior software developer in Python programming."},
    {"role": "user", "content": task_prompt+extra_message}
],
        response_format={"type": "text"},
        temperature=0.7,
        max_completion_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Extract and return the assistant's reply
    return response.choices[0].message.content

def save_results_to_csv(results, output_file):
    
    with open(output_file, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["task_index", "assistant_response"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in results:
            writer.writerow(entry)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Load all tasks from the CSV file
    tasks = load_humaneval_tasks("data/humaneval.csv")
    
    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # change as needed
    end_index = 2    # change as needed
    
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
    
    # Save all results to a CSV file
    save_results_to_csv(results, "responses_expert_humaneval.csv")