import zipfile
import os


class ZipFileProcessor:
    """
    A class for processing zip files, allowing reading, extracting, and creating zip files.
    """

    def __init__(self, file_name: str):
        """
        Initialize the ZipFileProcessor with the specified zip file name.
        
        :param file_name: The name of the zip file to process.
        """
        self.file_name = file_name

    def _is_valid(self) -> bool:
        """ Check if the file name is valid. """
        return bool(self.file_name)

    def read_zip_file(self) -> zipfile.ZipFile:
        """
        Opens the zip file for reading.
        
        :return: An open ZipFile object if successful, None otherwise.
        """
        if not self._is_valid():
            return None
        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except (FileNotFoundError, zipfile.BadZipFile):
            return None

    def extract_all(self, output_path: str) -> bool:
        """
        Extracts all files from the zip file to the specified output path.
        
        :param output_path: The directory where files will be extracted.
        :return: True if successful, False otherwise.
        """
        if not self._is_valid() or not output_path:
            return False
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile):
            return False

    def extract_file(self, file_name: str, output_path: str) -> bool:
        """
        Extracts a specific file from the zip file to the specified output path.
        
        :param file_name: The name of the file to extract.
        :param output_path: The directory where the file will be extracted.
        :return: True if successful, False otherwise.
        """
        if not self._is_valid() or not file_name or not output_path:
            return False
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extract(file_name, output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile, KeyError):
            return False

    def create_zip_file(self, files: list, output_file_name: str) -> bool:
        """
        Creates a zip file containing the specified files.
        
        :param files: List of file paths to include in the zip file.
        :param output_file_name: The name of the zip file to create.
        :return: True if successful, False otherwise.
        """
        if not files or not output_file_name:
            return False
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_ref:
                for file in files:
                    zip_ref.write(file, os.path.basename(file))
            return True
        except FileNotFoundError:
            return False