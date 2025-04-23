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
        if not isinstance(file_path, str):
            raise TypeError("file_path must be a string")
        self.file_path = file_path

    def read_file_as_json(self):
        """
        Read the file as JSON. If the file content is not valid JSON,
        attempt to read it as a simple type (int, float, or string).

        :return: A dictionary if the file contains JSON, an integer if the file
                 contains an integer, a float if the file contains a float, or
                 a string if the file contains a string.  Raises ValueError if
                 the file cannot be interpreted.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file content cannot be interpreted.
        """
        try:
            with open(self.file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    f.seek(0)  # Reset file pointer to the beginning
                    content = f.read().strip()
                    try:
                        return int(content)
                    except ValueError:
                        try:
                            return float(content)
                        except ValueError:
                            # Attempt to remove surrounding quotes if present
                            if content.startswith('"') and content.endswith('"'):
                                return content[1:-1]
                            else:
                                return content  # Return as is if not quoted
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            raise ValueError(f"Could not read file as JSON or simple type: {e}")


    def read_file(self):
        """
        Read the content of the file.

        :return: The content of the file as a string.
        :raises FileNotFoundError: If the file does not exist.
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def write_file(self, content):
        """
        Write content to the file, overwriting any existing content.

        :param content: The content to write to the file (string).
        :raises TypeError: If content is not a string.
        """
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        try:
            with open(self.file_path, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")


    def process_file(self):
        """
        Read the file, remove non-alphabetic characters, and overwrite the file
        with the processed content.

        :return: The processed content (string).
        :raises FileNotFoundError: If the file does not exist.
        """
        try:
            content = self.read_file()
            processed_content = re.sub(r'[^a-zA-Z]', '', content)
            self.write_file(processed_content)
            return processed_content
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"Error processing file: {e}")
            return None