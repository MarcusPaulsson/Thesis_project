import zipfile
import os


class ZipFileProcessor:
    """
    This is a compressed file processing class that provides the ability to read and decompress compressed files.
    """

    def __init__(self, file_name):
        """
        Initialize file name.
        :param file_name: string
        """
        self.file_name = file_name

    def read_zip_file(self):
        """
        Get open file object.
        :return: If successful, returns the open file object; otherwise, returns None.
        """
        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except (FileNotFoundError, zipfile.BadZipFile) as e:
            print(f"Error opening zip file: {e}")
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path.
        :param output_path: string, The location of the extracted file.
        :return: True if successful, False otherwise.
        """
        with self.read_zip_file() as zip_file:
            if zip_file:
                try:
                    zip_file.extractall(output_path)
                    return True
                except Exception as e:
                    print(f"Error extracting files: {e}")
                    return False
        return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path.
        :param file_name: string, The name of the file to be uncompressed.
        :param output_path: string, The location of the extracted file.
        :return: True if successful, False otherwise.
        """
        with self.read_zip_file() as zip_file:
            if zip_file:
                try:
                    zip_file.extract(file_name, output_path)
                    return True
                except KeyError:
                    print(f"File {file_name} not found in zip.")
                except Exception as e:
                    print(f"Error extracting file: {e}")
        return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path.
        :param files: list of string, List of files to compress.
        :param output_file_name: string, Specified output path.
        :return: True if successful, False otherwise.
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    if os.path.exists(file):
                        zip_file.write(file, os.path.basename(file))
                    else:
                        print(f"File {file} does not exist.")
            return True
        except Exception as e:
            print(f"Error creating zip file: {e}")
            return False