import json
import os

class JSONProcessor:
    """
    A class to process JSON files, including reading, writing, and modifying JSON data by removing a specified key.
    """

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        
        :param file_path: str, the path of the JSON file.
        :return: dict or None, the data from the JSON file if read successfully, 
                 None if the file does not exist, or raises an error if reading fails.
        """
        if not os.path.isfile(file_path):
            return None
        
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error reading JSON: {e}")

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: bool, True if the writing process is successful, raises an error if writing fails.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError as e:
            raise IOError(f"Error writing JSON: {e}")

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: bool, True if the specified key is successfully removed and the data is written back, 
                      raises an error if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)
        if data is None:
            raise FileNotFoundError(f"{file_path} does not exist.")
        
        if remove_key not in data:
            raise KeyError(f"{remove_key} does not exist in the JSON data.")
        
        del data[remove_key]
        self.write_json(data, file_path)
        return True