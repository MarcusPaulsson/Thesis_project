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
        Read the self.file_path file as json format.
        If the file content doesn't obey json format, attempt to parse it as a literal.
        If both fail, return the content as a string.
        :return: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
                return json.loads(content)
        except json.JSONDecodeError:
            try:
                with open(self.file_path, 'r') as f:
                    content = f.read()
                    return eval(content)
            except (NameError, SyntaxError, TypeError):
                with open(self.file_path, 'r') as f:
                    content = f.read()
                    return content

    def read_file(self):
        """
        Read the content of self.file_path file.
        :return: the content of the file as a string.
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: the content to write to the file.
        """
        try:
            with open(self.file_path, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        :return: The processed content.
        """
        content = self.read_file()
        if content is None:
            return None

        processed_content = ''.join(re.findall(r'[a-zA-Z]+', content))
        self.write_file(processed_content)
        return processed_content