import os
import sys
import json


# Adjust paths as needed
upper_main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_dir)
sys.path.append(upper_dir)



from extract_code_python import extract_and_save_python_code, save_results_to_json
import prompt_technique_templates as prompt
results = [
        {"task_index": "task1", "assistant_response": "Here is a response with ```python\nprint('Hello, world!')\n```"},
        {"task_index": "task2", "assistant_response": "Another response with ```python\ndef add(a, b):\n    return a + b\n``` and some other text."},
        {"task_index": "task3", "assistant_response": "\n\n[ANS]Here's the implementation of bubble sort in Python:\n\n```python\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n```\n\nThis implementation of bubble sort takes an array `arr` as input and sorts it in ascending order using the bubble sort algorithm. It works by repeatedly swapping adjacent elements if they are in the wrong order. The outer loop runs `n` times, where `n` is the length of the array, and the inner loop runs `n-i-1` times, where `i` is the current iteration of the outer loop. This is because after each iteration, the largest element will \"bubble up\" to the end of the array, so we don't need to check it again. "},
        
    ]
print(results)
# results_dir = os.path.join("results", "WizardCoder", "APPS", prompt.PROMPT_TECHNIQUE_SETTING)  # Adjust directory as needed.
# os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists.
# json_file_path = os.path.join(results_dir, "apps_raw.json")
# save_results_to_json(results, json_file_path)
# extract_and_save_python_code(json_file_path, results_dir)