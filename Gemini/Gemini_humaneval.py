import csv
from google import genai
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

def run_task_with_gemini(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the Gemini API.
    """
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    extra_message = "Give only the code."
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=task_prompt + extra_message
    )
    
    # Extract and return the assistant's reply
    return response.text

def save_results_to_csv(results, output_file):
    """
    Save the AI-generated responses to a CSV file.
    """
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
    end_index = 40    # change as needed
    
    results = []  # List to hold responses for each task
    
    # Loop through the selected task indices
    for i in range(start_index, end_index):
        task_prompt = tasks[i]
        print(f"Processing task {i}...")
        
        # Call the API for this task prompt
        assistant_response = run_task_with_gemini(task_prompt)
        
        # Save the result in the results list
        results.append({
            "task_index": i,
            "assistant_response": assistant_response
        })
    
    # Save all results to a CSV file
    save_results_to_csv(results, "Gemini_responses_expert_humaneval.csv")