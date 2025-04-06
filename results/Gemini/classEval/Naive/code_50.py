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
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        """
        if not os.path.exists(file_path):
            return 0

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return -1

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)  # Use indent for readability
            return 1
        except Exception as e:
            print(f"Error writing JSON file: {e}")
            return -1

    def process_json(self, file_path, remove_key):
        """
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)

        if data == 0:
            return 0

        if data == -1:
            return -1  # Or handle the error differently

        if remove_key in data:
            del data[remove_key]
            if self.write_json(data, file_path) == 1:
                return 1
            else:
                return -1 # Indicate writing error
        else:
            return 0  # Key not found
        
if __name__ == '__main__':
    # Example Usage (requires a file named 'test.json' in the same directory for the process_json example)
    processor = JSONProcessor()

    # Example 1: Writing to a JSON file
    data_to_write = {'key1': 'value1', 'key2': 'value2'}
    write_result = processor.write_json(data_to_write, 'test.json')
    print(f"Write result: {write_result}")  # Output: Write result: 1

    # Example 2: Reading from a JSON file
    read_data = processor.read_json('test.json')
    print(f"Read data: {read_data}")  # Output: Read data: {'key1': 'value1', 'key2': 'value2'}

    # Example 3: Processing a JSON file (removing a key)
    process_result = processor.process_json('test.json', 'key1')
    print(f"Process result: {process_result}")  # Output: Process result: 1

    # Verify the change
    read_data_after_process = processor.read_json('test.json')
    print(f"Read data after process: {read_data_after_process}") # Output: Read data after process: {'key2': 'value2'}

    # Example that handles file not existing
    read_result_nonexistent = processor.read_json('nonexistent.json')
    print(f"Read result nonexistent file: {read_result_nonexistent}")

    # Example where the key doesn't exist
    process_result_no_key = processor.process_json('test.json', 'key3')
    print(f"Process result no key: {process_result_no_key}")