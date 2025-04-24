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
        Read the self.file_path file as JSON format.
        If the file content doesn't obey JSON format, an error will be raised.
        :return: dict if the file is stored as JSON format, or str/int/float according to the file content otherwise.
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
            return json.loads(content)

    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: str
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        """
        Write content into the self.file_path file, overwriting if the file already exists.
        :param content: str
        """
        with open(self.file_path, 'w') as file:
            file.write(content)

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the processed data into the same self.file_path file.
        :return: str
        """
        content = self.read_file()
        processed_content = re.sub(r'[^a-zA-Z]', '', content)
        self.write_file(processed_content)
        return processed_content