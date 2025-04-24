import csv
import os

class CSVProcessor:
    """
    A class for processing CSV files, including reading, writing, and processing specific operations.
    """

    def read_csv(self, file_name):
        """
        Read a CSV file and return the title and data.
        
        :param file_name: str, name of the CSV file
        :return: tuple (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                title = next(reader)
                data = list(reader)
            return title, data
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a CSV file.
        
        :param data: list of lists, data to write
        :param file_name: str, name of the CSV file
        :return: int, 1 if success, 0 otherwise
        """
        if not data or not file_name:
            return 0
        
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Process a CSV file to retain only the N-th column, capitalizing the values.
        
        :param N: int, the N-th column (0-indexed)
        :param save_file_name: str, the name of the file to be processed
        :return: int, 1 if success, 0 otherwise
        """
        title, data = self.read_csv(save_file_name)
        if not title or not data or N >= len(title):
            return 0
        
        processed_data = [[row[N].upper()] for row in data]
        new_file_name = f"{os.path.splitext(save_file_name)[0]}_process.csv"
        
        if self.write_csv([title], new_file_name) == 1:
            return self.write_csv(processed_data, new_file_name)
        
        return 0