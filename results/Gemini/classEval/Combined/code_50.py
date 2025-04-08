import json
import os

class JSONProcessor:
    """
    A class to process JSON files, including reading, writing, and removing keys.
    """

    def read_json(self, file_path):
        """
        Reads a JSON file and returns the data.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The data from the JSON file if read successfully.
            int: 0 if the file does not exist.
            int: -1 if an error occurs during the reading process (e.g., invalid JSON).
        """
        if not os.path.exists(file_path):
            return 0

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            return -1
        except Exception:
            return -1

    def write_json(self, data, file_path):
        """
        Writes data to a JSON file.

        Args:
            data (dict): The data to be written to the JSON file.
            file_path (str): The path to the JSON file.

        Returns:
            int: 1 if the writing process is successful.
            int: -1 if an error occurs during the writing process.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  # Add indent for readability
            return 1
        except Exception:
            return -1

    def process_json(self, file_path, remove_key):
        """
        Reads a JSON file, removes a specified key, and rewrites the modified data back to the file.

        Args:
            file_path (str): The path to the JSON file.
            remove_key (str): The key to be removed.

        Returns:
            int: 1 if the specified key is successfully removed and the data is written back.
            int: 0 if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)

        if data == 0:
            return 0

        if data == -1:  # Handle JSONDecodeError or other read errors
            return 0

        if isinstance(data, dict) and remove_key in data:
            del data[remove_key]
            if self.write_json(data, file_path) == 1:
                return 1
            else:
                return 0
        else:
            return 0