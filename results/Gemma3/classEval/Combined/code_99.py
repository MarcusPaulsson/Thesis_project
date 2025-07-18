import zipfile
import os


class ZipFileProcessor:
    """
    This is a compressed file processing class that provides the ability to read and decompress compressed files
    """

    def __init__(self, file_name):
        """
        Initialize file name
        :param file_name:string
        """
        self.file_name = file_name

    def read_zip_file(self):
        """
        Get open file object
        :return:If successful, returns the open file object; otherwise, returns None
        """
        try:
            if not self.file_name:
                return None
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except FileNotFoundError:
            return None
        except zipfile.BadZipFile:
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            if not self.file_name or not output_path:
                return False
            zip_file = self.read_zip_file()
            if zip_file:
                zip_file.extractall(output_path)
                zip_file.close()
                return True
            else:
                return False
        except Exception:
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            if not self.file_name or not file_name or not output_path:
                return False
            zip_file = self.read_zip_file()
            if zip_file:
                zip_file.extract(file_name, output_path)
                zip_file.close()
                return True
            else:
                return False
        except KeyError:
            return False
        except Exception:
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        """
        try:
            if not files or not output_file_name:
                return False
            with zipfile.ZipFile(output_file_name, 'w') as zip_file:
                for file in files:
                    zip_file.write(file, os.path.basename(file))
            return True
        except Exception:
            return False