import json
import re
import os

# helper scripts for mid-process the output result from infernce

def extract_and_save_python_code(json_file, output_dir):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data)
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(data.items())

    # NEED TO BE REWRITTEN TO ONLY EXTRACT ONE SNIPPET PER FILE!!! CURRENTLY OVERWRITING
    for key, value in data.items():
        # Use an "or" condition to match both patterns
        try:
            code_blocks = re.findall(r'```python\n(.*?)\n```|```python\s*(.*?)\s*```', value, re.DOTALL)
            
        except:
            pass
        if code_blocks:
            for match in code_blocks:
                # Determine which group matched (original or flexible)
                code = match[0] if match[0] else match[1]

                # Clean up the code (remove extra spaces/newlines)
                cleaned_code = code.strip()

                # Create a file name based on the key
                file_name = f"code_{key}.py"
                file_path = os.path.join(output_dir, file_name)

                try:
                    with open(file_path, 'w', encoding='utf-8') as py_file:
                        py_file.write(cleaned_code)
                    print(f"Saved code block from key '{key}' to '{file_path}'")
                except Exception as e:
                    print(f"Error saving code block from key '{key}': {e}")
        else:
            print(f"No Python code blocks found in key '{key}'.")




def save_results_to_json(results, output_file):
    output_data = {}
    for entry in results:
        output_data[entry["task_index"]] = entry["assistant_response"]

    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile, ensure_ascii=False, indent=4) #ensure_ascii=False ensures non-ascii characters are correctly saved.
    print(f"Results saved to {output_file}")


# Example usage:
if __name__ == "__main__":

    # Example Results List (Replace with your actual data)
    results = [
        {"task_index": "task1", "assistant_response": "Here is a response with ```python\nprint('Hello, world!')\n```"},
        {"task_index": "task2", "assistant_response": "Another response with ```python\ndef add(a, b):\n    return a + b\n``` and some other text."},
        {"task_index": "task3", "assistant_response": "\n\n[ANS]Here's the implementation of bubble sort in Python:\n\n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n```\n\nThis implementation of bubble sort takes an array `arr` as input and sorts it in ascending order using the bubble sort algorithm. It works by repeatedly swapping adjacent elements if they are in the wrong order. The outer loop runs `n` times, where `n` is the length of the array, and the inner loop runs `n-i-1` times, where `i` is the current iteration of the outer loop. This is because after each iteration, the largest element will \"bubble up\" to the end of the array, so we don't need to check it again. "},
        
    ]

    # Save results to a JSON file
    json_file_path = 'test_chatGPT_cli_games.json'
    save_results_to_json(results, json_file_path)

    # Extract and save Python code from the saved JSON
    output_directory = 'results/WizardCoder/APPS/Zero-shot'
    extract_and_save_python_code(json_file_path, output_directory)

