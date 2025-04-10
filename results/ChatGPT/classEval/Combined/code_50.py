import json
import os

class JSONProcessor:
    """
    A class to process JSON files, including reading, writing, and modifying JSON data.
    """

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        
        :param file_path: str, the path of the JSON file.
        :return: dict or int, the data from the JSON file if read successfully, 
                -1 if an error occurs, or 0 if the file does not exist.
        """
        if not os.path.isfile(file_path):
            return 0
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return -1

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: int, 1 if successful, -1 if an error occurs.
        """
        if not isinstance(data, dict) or not file_path:
            return -1
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return 1
        except (IOError, TypeError):
            return -1

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file, remove a specified key, and write the modified data back.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: int, 1 if the key was removed and data written back, 
                0 if the file does not exist or key does not exist in the data.
        """
        data = self.read_json(file_path)
        if data in (0, -1) or remove_key not in data:
            return 0

        data.pop(remove_key, None)  # Remove the key if it exists
        return self.write_json(data, file_path)