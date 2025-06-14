import json
import os

class JSONProcessor:
    """
    This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.
    """

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :param file_path: str, the path of the JSON file.
        :return: dict, the data from the JSON file if read successfully, or None if an error occurs during the reading process.
                    return None if the file does not exist.
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
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: True if the writing process is successful, or False if an error occurs during the writing process.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  # Add indent for readability
            return 1
        except Exception:
            return -1

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: True, if the specified key is successfully removed and the data is written back.
                    False, if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)

        if data == 0:
            return 0

        if data == -1:
            return 0

        if remove_key in data:
            del data[remove_key]
            if self.write_json(data, file_path) == 1:
                return 1
            else:
                return 0
        else:
            return 0