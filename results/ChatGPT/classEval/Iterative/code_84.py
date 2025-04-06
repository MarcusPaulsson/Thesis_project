import json
import re
import os

class TextFileProcessor:
    """
    The class handles reading, writing, and processing text files. It can read the file as JSON,
    read the raw text, write content to the file, and process the file by removing non-alphabetic characters.
    """

    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        if not isinstance(file_path, str):
            raise ValueError("File path must be a string.")
        self.file_path = file_path

    def read_file_as_json(self):
        """
        Read the self.file_path file as json format.
        If the file content doesn't obey json format, it raises a JSONDecodeError.
        :return: dict if the file is stored as json format, or raises an error otherwise.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path}'")
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: the same return as the read() method
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No such file: '{self.file_path}'")
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        """
        Write content into the self.file_path file, overwriting if the file already exists.
        :param content: str
        """
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        with open(self.file_path, 'w') as file:
            file.write(content)

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the processed data into the same self.file_path file.
        :return: the processed content string
        """
        content = self.read_file()
        processed_content = ''.join(re.findall(r'[a-zA-Z]', content))
        self.write_file(processed_content)
        return processed_content