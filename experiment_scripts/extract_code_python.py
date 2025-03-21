import json
import re
import os

# helper scripts for mid-process the output result from infernce

def extract_and_save_python_code(json_file, output_dir):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

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
        {"task_index": "task3", "assistant_response": "No code here."},
    ]

    # Save results to a JSON file
    json_file_path = 'test_chatGPT_cli_games.json'
    save_results_to_json(results, json_file_path)

    # Extract and save Python code from the saved JSON
    output_directory = 'results/ChatGPT/cli_games'
    extract_and_save_python_code(json_file_path, output_directory)

    # Example usage with a different JSON file
    json_file_path = 'test.json'  # Replace with your JSON file path
    # Create a dummy test.json.
    with open(json_file_path, 'w') as f:
        json.dump({"test_key":"here is some code ```python\nprint('test')\n```"}, f)
    output_directory = ''
    extract_and_save_python_code(json_file_path, output_directory)
