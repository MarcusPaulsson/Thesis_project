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
            zip_file = zipfile.ZipFile(self.file_name, 'r')
            return zip_file
        except FileNotFoundError:
            print(f"Error: File not found: {self.file_name}")
            return None
        except zipfile.BadZipFile:
            print(f"Error: Invalid zip file: {self.file_name}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def extract_all(self, output_path):
        """
        Extract all zip files and place them in the specified path
        :param output_path: string, The location of the extracted file
        :return: True or False, representing whether the extraction operation was successful
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                zip_file.extractall(output_path)
            return True
        except FileNotFoundError:
            print(f"Error: File not found: {self.file_name}")
            return False
        except zipfile.BadZipFile:
            print(f"Error: Invalid zip file: {self.file_name}")
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
        """
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_file:
                for file_info in zip_file.infolist():
                    if file_info.filename == file_name:
                        zip_file.extract(file_info, output_path)
                        return True
                print(f"Error: File '{file_name}' not found in the zip archive.")
                return False
        except FileNotFoundError:
            print(f"Error: File not found: {self.file_name}")
            return False
        except zipfile.BadZipFile:
            print(f"Error: Invalid zip file: {self.file_name}")
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
        """
        try:
            with zipfile.ZipFile(output_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file in files:
                    if os.path.exists(file):
                        zip_file.write(file)
                    else:
                        print(f"Warning: File not found: {file}")
                        return False
            return True
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False


if __name__ == '__main__':
    # Example usage (requires dummy files and directories)
    # Create dummy files for testing
    if not os.path.exists("test1.txt"):
        with open("test1.txt", "w") as f:
            f.write("This is test file 1.")
    if not os.path.exists("test2.txt"):
        with open("test2.txt", "w") as f:
            f.write("This is test file 2.")
    if not os.path.exists("test3.txt"):
        with open("test3.txt", "w") as f:
            f.write("This is test file 3.")

    # Create a zip file
    zfp = ZipFileProcessor("my_archive.zip")
    files_to_zip = ["test1.txt", "test2.txt", "test3.txt"]
    if zfp.create_zip_file(files_to_zip, "my_archive.zip"):
        print("Zip file created successfully.")

    # Read the zip file
    zip_file_obj = zfp.read_zip_file()
    if zip_file_obj:
        print("Zip file opened successfully.")
        zip_file_obj.close()

    # Extract all files
    output_dir = "extracted_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if zfp.extract_all(output_dir):
        print("All files extracted successfully.")

    # Extract a specific file
    specific_file = "test2.txt"
    output_dir_single = "extracted_single"
    if not os.path.exists(output_dir_single):
        os.makedirs(output_dir_single)

    if zfp.extract_file(specific_file, output_dir_single):
        print(f"File '{specific_file}' extracted successfully.")