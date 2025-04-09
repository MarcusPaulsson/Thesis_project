import json

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
        If the file content doesn't obey json format, attempt to parse as int or float, otherwise return as string.
        :return: dict if the file is stored as json format, or str/int/float otherwise.
        """
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError:
            with open(self.file_path, 'r') as f:
                content = f.read()
                try:
                    return int(content)
                except ValueError:
                    try:
                        return float(content)
                    except ValueError:
                        return content

    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: the content of the file as a string.
        """
        with open(self.file_path, 'r') as f:
            return f.read()

    def write_file(self, content):
        """
        Write content into the self.file_path file, overwriting if the file already exists.
        :param content: any content to be written to the file.
        """
        with open(self.file_path, 'w') as f:
            f.write(str(content))

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the processed data into the same self.file_path file.
        :return: The processed string with only alphabetic characters.
        """
        content = self.read_file()
        processed_content = ''.join(char for char in content if char.isalpha())
        self.write_file(processed_content)
        return processed_content