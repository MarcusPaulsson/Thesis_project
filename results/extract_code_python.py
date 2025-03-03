import json
import re
import os

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
        # Find code blocks enclosed in triple backticks
        code_blocks = re.findall(r'```python\n(.*?)\n```', value, re.DOTALL)

        if code_blocks:
            for i, code in enumerate(code_blocks):
                # Clean up the code (remove extra spaces/newlines)
                cleaned_code = code.strip()

                # Create a file name based on the key
                file_name = f"code_{key}.py"
                file_path = os.path.join(output_dir, file_name)

                try:
                    with open(file_path, 'w', encoding='utf-8') as py_file:
                        py_file.write(cleaned_code)
                    print(f"Saved code block from key '{key}' to '{file_path}'") #removed the i from the print statement.
                except Exception as e:
                    print(f"Error saving code block from key '{key}': {e}") #removed the i from the print statement.
        else:
            print(f"No Python code blocks found in key '{key}'.")

# Example usage:
if __name__ == "__main__":
    json_file_path = 'test.json'  # Replace with your JSON file path
    output_directory = 'results/Gemini/cli_games' #where the python files will be saved.

    extract_and_save_python_code(json_file_path, output_directory)
