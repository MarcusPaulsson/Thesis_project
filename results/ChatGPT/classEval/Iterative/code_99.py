import zipfile
import os


class ZipFileProcessor:
    """
    A class to process zip files, providing functionality to read, extract, and create zip files.
    """

    def __init__(self, file_name):
        """
        Initialize with the zip file name.
        
        :param file_name: str, name of the zip file.
        """
        self.file_name = file_name

    def _is_valid_zip(self):
        """Check if the given file is a valid zip file."""
        return os.path.isfile(self.file_name) and zipfile.is_zipfile(self.file_name)

    def read_zip_file(self):
        """
        Open and return the zip file object if valid; otherwise, return None.
        
        :return: zipfile.ZipFile or None
        """
        if self._is_valid_zip():
            return zipfile.ZipFile(self.file_name, 'r')
        return None

    def extract_all(self, output_path):
        """
        Extract all contents of the zip file to the specified output path.
        
        :param output_path: str, directory where files will be extracted.
        :return: bool, True if extraction is successful, otherwise False.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile, PermissionError) as e:
            print(f"Error extracting zip file: {e}")
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract a specific file from the zip file to the specified output path.
        
        :param file_name: str, name of the file to be extracted.
        :param output_path: str, directory where the file will be extracted.
        :return: bool, True if extraction is successful, otherwise False.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extract(file_name, output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile, KeyError, PermissionError) as e:
            print(f"Error extracting file '{file_name}': {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Create a zip file containing the specified list of files.
        
        :param files: list of str, list of file paths to compress.
        :param output_file_name: str, path where the output zip file will be created.
        :return: bool, True if compression is successful, otherwise False.
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_ref:
                for file in files:
                    if os.path.isfile(file):
                        zip_ref.write(file, os.path.basename(file))
                    else:
                        print(f"File '{file}' not found, skipping.")
            return True
        except (IOError, PermissionError) as e:
            print(f"Error creating zip file: {e}")
            return False