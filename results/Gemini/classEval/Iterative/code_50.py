import json
import os

class JSONProcessor:
    """
    This class processes JSON files, including reading, writing, and modifying data.
    """

    def read_json(self, file_path):
        """
        Reads a JSON file and returns the data as a dictionary.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The JSON data as a dictionary.
            None: If the file does not exist or an error occurs during reading.
        """
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return None

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def write_json(self, data, file_path):
        """
        Writes data to a JSON file.

        Args:
            data (dict): The data to write to the JSON file.
            file_path (str): The path to the JSON file.

        Returns:
            bool: True if the writing process is successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error writing JSON to file: {e}")
            return False

    def process_json(self, file_path, remove_key):
        """
        Reads a JSON file, removes a specified key, and writes the modified data back to the file.

        Args:
            file_path (str): The path to the JSON file.
            remove_key (str): The key to remove from the JSON data.

        Returns:
            bool: True if the key was successfully removed and the data was written back, False otherwise.
        """
        data = self.read_json(file_path)

        if data is None:
            return False

        if remove_key in data:
            del data[remove_key]
            if self.write_json(data, file_path):
                return True
            else:
                return False
        else:
            print(f"Key '{remove_key}' not found in JSON data.")
            return False