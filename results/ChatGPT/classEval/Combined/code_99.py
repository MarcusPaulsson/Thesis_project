import zipfile
import os


class ZipFileProcessor:
    """
    A class to process ZIP files, providing functionalities for reading,
    extracting, and creating ZIP files.
    """

    def __init__(self, file_name):
        """
        Initialize with the path to the ZIP file.
        :param file_name: str - The ZIP file path.
        """
        self.file_name = file_name

    def _validate_zip_file(self):
        """Check if the ZIP file exists and is valid."""
        return os.path.exists(self.file_name) and zipfile.is_zipfile(self.file_name)

    def read_zip_file(self):
        """
        Open the ZIP file and return the file object.
        :return: zipfile.ZipFile or None if the file is invalid.
        """
        if not self._validate_zip_file():
            return None
        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except zipfile.BadZipFile:
            return None

    def extract_all(self, output_path):
        """
        Extract all files from the ZIP file to the specified output path.
        :param output_path: str - The directory where files will be extracted.
        :return: bool - True if extraction is successful, False otherwise.
        """
        if not self._validate_zip_file() or not output_path:
            return False
        os.makedirs(output_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except Exception:
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract a specific file from the ZIP file to the specified output path.
        :param file_name: str - The name of the file to extract.
        :param output_path: str - The directory where the file will be extracted.
        :return: bool - True if extraction is successful, False otherwise.
        """
        if not self._validate_zip_file() or not file_name or not output_path:
            return False
        os.makedirs(output_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extract(file_name, output_path)
            return True
        except (KeyError, zipfile.BadZipFile):
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Create a ZIP file from a list of files.
        :param files: list of str - The files to compress.
        :param output_file_name: str - The name of the output ZIP file.
        :return: bool - True if creation is successful, False otherwise.
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