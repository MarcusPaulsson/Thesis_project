import zipfile
import os


class ZipFileProcessor:
    """
    A class to handle zip file operations including reading, extracting, and creating zip files.
    """

    def __init__(self, file_name):
        """
        Initialize the ZipFileProcessor with the specified zip file name.
        
        :param file_name: str, the name of the zip file to process
        """
        self.file_name = file_name

    def _is_valid(self):
        """Check if the file name is valid."""
        return bool(self.file_name)

    def read_zip_file(self):
        """
        Open and return the zip file object.
        
        :return: zipfile.ZipFile or None if the file cannot be opened
        """
        if not self._is_valid():
            return None
        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except (FileNotFoundError, zipfile.BadZipFile):
            return None

    def extract_all(self, output_path):
        """
        Extract all files from the zip file to the specified output path.
        
        :param output_path: str, the directory where files will be extracted
        :return: bool, True if extraction was successful, False otherwise
        """
        if not self._is_valid() or not output_path:
            return False
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile):
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract a specific file from the zip file to the specified output path.
        
        :param file_name: str, the name of the file to extract
        :param output_path: str, the directory where the file will be extracted
        :return: bool, True if extraction was successful, False otherwise
        """
        if not self._is_valid() or not file_name or not output_path:
            return False
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extract(file_name, output_path)
            return True
        except (FileNotFoundError, zipfile.BadZipFile, KeyError):
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Create a zip file containing the specified list of files.
        
        :param files: list of str, the files to include in the zip
        :param output_file_name: str, the name of the output zip file
        :return: bool, True if the zip file was created successfully, False otherwise
        """
        if not files or not output_file_name:
            return False
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_ref:
                for file in files:
                    zip_ref.write(file, os.path.basename(file))
            return True
        except Exception:
            return False