import zipfile
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ZipFileProcessor:
    """
    A class for processing zip files, providing functionalities to read, extract, and create zip archives.
    """

    def __init__(self, file_name):
        """
        Initializes the ZipFileProcessor with the name of the zip file.

        Args:
            file_name (str): The name of the zip file to be processed.
        """
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")
        self.file_name = file_name
        logging.debug(f"ZipFileProcessor initialized with file: {file_name}")

    def read_zip_file(self):
        """
        Opens the zip file in read mode.

        Returns:
            zipfile.ZipFile: A ZipFile object if the file is successfully opened, None otherwise.
        """
        try:
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            logging.info(f"Successfully opened zip file: {self.file_name}")
            return zip_file
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_name}")
            return None
        except zipfile.BadZipFile:
            logging.error(f"Not a valid zip file: {self.file_name}")
            return None
        except Exception as e:
            logging.exception(f"An unexpected error occurred while reading {self.file_name}: {e}")
            return None

    def extract_all(self, output_path):
        """
        Extracts all files from the zip archive to the specified output path.

        Args:
            output_path (str): The directory where the files will be extracted.

        Returns:
            bool: True if the extraction was successful, False otherwise.
        """
        if not isinstance(output_path, str):
            raise TypeError("output_path must be a string")

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extractall(output_path)
            logging.info(f"Successfully extracted all files from {self.file_name} to {output_path}")
            return True
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_name}")
            return False
        except zipfile.BadZipFile:
            logging.error(f"Not a valid zip file: {self.file_name}")
            return False
        except Exception as e:
            logging.exception(f"An unexpected error occurred while extracting all from {self.file_name}: {e}")
            return False

    def extract_file(self, file_name, output_path):
        """
        Extracts a specific file from the zip archive to the specified output path.

        Args:
            file_name (str): The name of the file to extract.
            output_path (str): The directory where the file will be extracted.

        Returns:
            bool: True if the extraction was successful, False otherwise.
        """
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")
        if not isinstance(output_path, str):
            raise TypeError("output_path must be a string")

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extract(file_name, output_path)
            logging.info(f"Successfully extracted {file_name} from {self.file_name} to {output_path}")
            return True
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_name}")
            return False
        except zipfile.BadZipFile:
            logging.error(f"Not a valid zip file: {self.file_name}")
            return False
        except KeyError:
            logging.error(f"File {file_name} not found in the zip archive {self.file_name}")
            return False
        except Exception as e:
            logging.exception(f"An unexpected error occurred while extracting {file_name} from {self.file_name}: {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Creates a zip file containing the specified files.

        Args:
            files (list of str): A list of file paths to be added to the zip archive.
            output_file_name (str): The name of the zip file to be created (without the .zip extension).

        Returns:
            bool: True if the zip file was created successfully, False otherwise.
        """
        if not isinstance(files, list):
            raise TypeError("files must be a list")
        if not isinstance(output_file_name, str):
            raise TypeError("output_file_name must be a string")

        try:
            zip_file_path = output_file_name + ".zip"
            with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
                for file in files:
                    if not isinstance(file, str):
                        logging.warning(f"Skipping non-string file name: {file}")
                        continue

                    if os.path.exists(file):
                        zip_file.write(file)
                        logging.debug(f"Added {file} to {zip_file_path}")
                    else:
                        logging.warning(f"File not found, skipping: {file}")
            logging.info(f"Successfully created zip file: {zip_file_path}")
            return True
        except Exception as e:
            logging.exception(f"An unexpected error occurred while creating {output_file_name}.zip: {e}")
            return False


if __name__ == '__main__':
    # Example usage (create dummy files and then zip them)
    try:
        os.makedirs("output", exist_ok=True)  # Create 'output' directory if it doesn't exist
        os.makedirs("result/aaa", exist_ok=True)  # Create 'result/aaa' directory if it doesn't exist

        with open("bbb.txt", "w") as f:
            f.write("This is bbb.txt")
        with open("ccc.txt", "w") as f:
            f.write("This is ccc.txt")
        with open("ddd.txt", "w") as f:
            f.write("This is ddd.txt")

        zfp = ZipFileProcessor("aaa.zip")  # This line is not doing anything useful
        zfp = ZipFileProcessor("test.zip")
        zfp.create_zip_file(["bbb.txt", "ccc.txt", "ddd.txt"], "output/bcd")

        # Extract all files to result/aaa folder
        zfp = ZipFileProcessor("output/bcd.zip")
        zfp.extract_all("result/aaa")

        print("Example completed successfully.")

    except Exception as e:
        print(f"An error occurred during the example: {e}")