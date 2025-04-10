import json
import re
from typing import Union

class TextFileProcessor:
    """
    The class handles reading, writing, and processing text files.
    It can read the file as JSON, read the raw text, write content to the file,
    and process the file by removing non-alphabetic characters.
    """

    def __init__(self, file_path: str):
        """
        Initialize the file path.
        :param file_path: str - Path to the file to be processed.
        """
        self.file_path = file_path

    def read_file_as_json(self) -> Union[dict, str, int, float]:
        """
        Read the file at self.file_path as JSON.
        :return: Parsed JSON data (dict, str, int, float)
        :raises ValueError: If the file content is not valid JSON.
        """
        with open(self.file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format: {e}")

    def read_file(self) -> str:
        """
        Read and return the content of the file at self.file_path.
        :return: Content of the file as a string.
        """
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content: str) -> None:
        """
        Write content into the file at self.file_path, overwriting if the file already exists.
        :param content: str - Content to write to the file.
        """
        with open(self.file_path, 'w') as file:
            file.write(content)

    def process_file(self) -> str:
        """
        Read the file at self.file_path and filter out non-alphabetic characters from the content.
        Overwrite the processed data into the same self.file_path file.
        :return: Processed content string.
        """
        content = self.read_file()
        processed_content = re.sub(r'[^a-zA-Z]', '', content)
        self.write_file(processed_content)
        return processed_content