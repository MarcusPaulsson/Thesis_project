import json
import re

class TextFileProcessor:
    """
    The class handles reading, writing, and processing text files. It can read the file as JSON, read the raw text, write content to the file, and process the file by removing non-alphabetic characters.
    """

    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        self.file_path = file_path

    def read_file_as_json(self):
        """
        Read the file as JSON.  If the file is not valid JSON, return None.
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None

    def read_file(self):
        """
        Read the content of the file.
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_file(self, content):
        """
        Write content to the file, overwriting existing content.
        """
        try:
            with open(self.file_path, 'w') as f:
                f.write(content)
            return True  # Indicate success
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False #Indicate failure

    def process_file(self):
        """
        Read the file, remove non-alphabetic characters, and overwrite the file.
        Returns the processed content. Returns None if there is a file error.
        """
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()

            processed_content = ''.join(re.findall(r'[a-zA-Z]+', content))

            with open(self.file_path, 'w') as f:
                f.write(processed_content)

            return processed_content
        except FileNotFoundError:
            return None

if __name__ == '__main__':
    # Example Usage (and basic tests)
    test_file = "test_example.txt"

    # Test write_file
    processor = TextFileProcessor(test_file)
    if processor.write_file("This is a test."):
        print("write_file test: Success")
    else:
        print("write_file test: Failure")

    # Test read_file
    content = processor.read_file()
    if content == "This is a test.":
        print("read_file test: Success")
    else:
        print(f"read_file test: Failure, got: {content}")

    # Test process_file
    processor.write_file("Hello, World! 123")
    processed_content = processor.process_file()
    if processed_content == "HelloWorld":
        print("process_file test: Success")
    else:
        print(f"process_file test: Failure, got: {processed_content}")

    # Test read_file_as_json (valid JSON)
    processor.write_file('{"name": "John", "age": 30}')
    json_data = processor.read_file_as_json()
    if isinstance(json_data, dict) and json_data.get("name") == "John":
        print("read_file_as_json (valid) test: Success")
    else:
        print(f"read_file_as_json (valid) test: Failure, got: {json_data}")

    # Test read_file_as_json (invalid JSON)
    processor.write_file("This is not JSON")
    json_data = processor.read_file_as_json()
    if json_data is None:
        print("read_file_as_json (invalid) test: Success")
    else:
        print(f"read_file_as_json (invalid) test: Failure, got: {json_data}")

    import os
    try:
        os.remove(test_file) # Clean up the test file
    except OSError as e:
        print(f"Error deleting test file: {e}")