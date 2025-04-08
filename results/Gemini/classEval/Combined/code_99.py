import zipfile
import os


class ZipFileProcessor:
    """
    This is a compressed file processing class that provides the ability to read and decompress compressed files
    """

    def __init__(self, file_name):
        """
        Initialize file name
        :param file_name: string
        """
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")
        self.file_name = file_name

    def read_zip_file(self):
        """
        Get open file object
        :return: If successful, returns the open file object; otherwise, returns None
        """
        if not self.file_name:
            return None

        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except FileNotFoundError:
            return None
        except zipfile.BadZipFile:
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log the exception for debugging
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        if not isinstance(output_path, str):
            raise TypeError("output_path must be a string")

        if not self.file_name:
            return False

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extractall(output_path)
            return True
        except FileNotFoundError:
            return False
        except zipfile.BadZipFile:
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name: string, The name of the file to be uncompressed
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")
        if not isinstance(output_path, str):
            raise TypeError("output_path must be a string")

        if not self.file_name:
            return False

        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extract(file_name, output_path)
            return True
        except FileNotFoundError:
            return False
        except KeyError:
            return False
        except zipfile.BadZipFile:
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files: list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return: True or False, representing whether the compression operation was successful
        """
        if not isinstance(files, list):
            raise TypeError("files must be a list")
        if not isinstance(output_file_name, str):
            raise TypeError("output_file_name must be a string")

        if not files:
            return False

        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    if not isinstance(file, str):
                         print("file name must be a string")
                         return False
                    zip_file.write(file, os.path.basename(file))
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


if __name__ == '__main__':
    import unittest

    unittest.main()