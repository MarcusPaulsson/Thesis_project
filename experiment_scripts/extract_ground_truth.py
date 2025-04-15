import json
import os
import sys

upper_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(upper_dir)


def extract_classeval_ground_truth():
    solution_data_path = os.path.abspath(os.path.join(upper_dir,'data', 'ClassEval_data.json'))
    test_cases =[] 
    try:
        with open(solution_data_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                text = item["solution_code"]
                test_cases.append(text) # Assumes each item in the JSON list has a 'skeleton' key
        return test_cases
   
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

def extract_apps_ground_truth():
    solution_data_path = os.path.abspath(os.path.join('data', 'apps.json'))
    try:
        with open(solution_data_path, 'r', encoding='utf-8') as jsonfile:
            return [json.loads(line.strip()) for line in jsonfile if "solutions" in json.loads(line.strip())]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None
    
   
    

def save_ground_truth():
    classeval = extract_classeval_ground_truth()
    apps = extract_apps_ground_truth()

    if classeval:
        for i, item in enumerate(classeval):
            file_name = f"code_{i}.py"
            dir_name = os.path.abspath(os.path.join(upper_dir,'ground_truth', "classEval"))
            os.makedirs(dir_name, exist_ok=True)
            file_path = os.path.join(dir_name, file_name)
            try:
                with open(file_path, 'w', encoding='utf-8') as py_file:
                    py_file.write(item)
                print(f"Saved code block from ClassEval index '{i}' to '{file_path}'")
            except Exception as e:
                print(f"Error saving ClassEval code block at index '{i}': {e}")

    if apps:
        for i, item in enumerate(apps):
            file_name = f"code_{i}.py"
            dir_name = os.path.abspath(os.path.join(upper_dir,'ground_truth', "APPS"))
            os.makedirs(dir_name, exist_ok=True)
            file_path = os.path.join(dir_name, file_name)
            try:
                with open(file_path, 'w', encoding='utf-8') as py_file:
                    py_file.write(item['solutions'] if isinstance(item, dict) and 'solutions' in item and item['solutions'] else item) # Assuming you want the first solution
                print(f"Saved code block from APPS index '{i}' to '{file_path}'")
            except Exception as e:
                print(f"Error saving APPS code block at index '{i}': {e}")

save_ground_truth()

save_ground_truth()








