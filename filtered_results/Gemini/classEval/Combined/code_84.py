import json
import re

class TextFileProcessor:
    """
    Handles reading, writing, and processing text files.
    """

    def __init__(self, file_path):
        """
        Initializes the file path.
        :param file_path: str
        """
        self.file_path = file_path

    def read_file_as_json(self):
        """
        Reads the file as JSON. Returns a dictionary if the file contains valid JSON,
        otherwise attempts to evaluate the content as a Python literal. If both fail,
        returns the raw string content.
        :return: dict, str, int, float, or None
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            try:
                with open(self.file_path, 'r') as f:
                    content = f.read()
                    return eval(content)
            except (NameError, SyntaxError):
                with open(self.file_path, 'r') as f:
                    return f.read()
        except FileNotFoundError:
            return None


    def read_file(self):
        """
        Reads and returns the content of the file.
        :return: str or None
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_file(self, content):
        """
        Writes the given content to the file, overwriting any existing content.
        :param content: str
        """
        try:
            with open(self.file_path, 'w') as f:
                f.write(str(content))
        except Exception as e:
            print(f"Error writing to file: {e}")

    def process_file(self):
        """
        Reads the file, filters out non-alphabetic characters, writes the processed
        content back to the file, and returns the processed content.
        :return: str
        """
        try:
            content = self.read_file()
            if content is None:
                return ""

            processed_content = ''.join(re.findall(r'[a-zA-Z]', content))
            self.write_file(processed_content)
            return processed_content
        except Exception as e:
            print(f"Error processing file: {e}")
            return ""