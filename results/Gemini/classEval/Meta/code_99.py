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
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> file = zfp.read_zip_file()
        """
        try:
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return None
        except zipfile.BadZipFile:
            print(f"Error: '{self.file_name}' is not a valid zip file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_all("result/aaa")
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extractall(output_path)
            return True
        except FileNotFoundError:
            print(f"Error: Zip file '{self.file_name}' not found.")
            return False
        except zipfile.BadZipFile:
            print(f"Error: '{self.file_name}' is not a valid zip file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def extract_file(self, file_name, output_path):
        """
        Extract the file with the specified name from the zip file and place it in the specified path
        :param file_name:string, The name of the file to be uncompressed
        :param output_path:string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.extract_file("bbb.txt", "result/aaa")
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                try:
                    zip_file.extract(file_name, output_path)
                    return True
                except KeyError:
                    print(f"Error: File '{file_name}' not found in the zip archive.")
                    return False
        except FileNotFoundError:
            print(f"Error: Zip file '{self.file_name}' not found.")
            return False
        except zipfile.BadZipFile:
            print(f"Error: '{self.file_name}' is not a valid zip file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
        """
        try:
            with zipfile.ZipFile(output_file_name + ".zip", 'w') as zip_file:
                for file in files:
                    if os.path.exists(file):
                        zip_file.write(file)
                    else:
                        print(f"Warning: File '{file}' not found and will be skipped.")
                return True
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False