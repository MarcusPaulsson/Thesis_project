import csv
from openai import OpenAI
import config

def load_classEval_tasks(csv_file_path):
  
    tasks = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append(row["skeleton"])
    return tasks

def run_task_with_api(task_prompt):
    """
    Run a single task by passing the task prompt as the user's message
    to the OpenAI API.
    """
    client = OpenAI(api_key=config.OPENAI_API_KEY)
    extra_message = " Give only the code."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior software developer in Python programming."},
            {"role": "user", "content": task_prompt + extra_message}
        ],
        response_format={"type": "text"},
        temperature=0.7,
        max_completion_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    total_tokens = response.usage.total_tokens
    print("Token count:", total_tokens)
    return response.choices[0].message.content

def save_results_to_json(results, output_file):
    output_data = {}
    for entry in results:
        output_data[entry["task_index"]] = entry["assistant_response"]

    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile, ensure_ascii=False, indent=4) #ensure_ascii=False ensures non-ascii characters are correctly saved.
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Load all tasks from the ClassEval CSV file
    tasks = load_classEval_tasks("data/classeval.csv")
    
    # Define the index interval for tasks you want to run (start_index inclusive, end_index exclusive)
    start_index = 0  # Change as needed
    end_index = 1    # Change as needed
    
    results = []  # List to hold responses for each task
    
    # Loop through the selected task indices
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
    save_file = 
    save_results_to_json(results, "responses_expert_classeval.csv")
