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
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            with open(self.file_path, 'r') as f:
                content = f.read()
                try:
                    return json.loads(content)
                except:
                    try:
                        return int(content)
                    except:
                        try:
                            return float(content)
                        except:
                            content = content.strip()
                            if content.startswith('"') and content.endswith('"'):
                                return content[1:-1]
                            else:
                                return content

    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        """
        try:
            with open(self.file_path, 'w') as f:
                f.write(str(content))
        except Exception as e:
            print(f"Error writing to file: {e}")

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
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