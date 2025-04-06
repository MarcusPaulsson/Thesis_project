import csv
import os

class CSVProcessor:
    """
    A class for processing CSV files, including reading and writing CSV data,
    as well as performing specific operations and saving the results to a new CSV file.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the CSV file specified by file_name and return the title and data.
        
        :param file_name: str, name of the CSV file
        :return: tuple (list, list), where the first element is the title and the second is the data
        """
        try:
            with open(file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                title = next(reader)
                data = [row for row in reader]
            return title, data
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return [], []
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a CSV file.
        
        :param data: list of lists, data to be written to the CSV file
        :param file_name: str, name of the CSV file
        :return: int, if successful return 1, otherwise return 0
        """
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except Exception as e:
            print(f"An error occurred while writing to the CSV file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a CSV file, capitalize the N-th column data, and save it to a new CSV file.
        
        :param N: int, the N-th column (0-indexed)
        :param save_file_name: str, the name of the file that needs to be processed
        :return: int, if successful return 1, otherwise return 0
        """
        try:
            title, data = self.read_csv(save_file_name)
            if not data or N >= len(title):
                print("Error: No data to process or invalid column index.")
                return 0
            
            new_data = [[row[N].upper()] for row in data if len(row) > N]
            new_file_name = os.path.splitext(save_file_name)[0] + '_process.csv'
            self.write_csv([title], new_file_name)
            self.write_csv(new_data, new_file_name)
            return 1
        except Exception as e:
            print(f"An error occurred during processing: {e}")
            return 0