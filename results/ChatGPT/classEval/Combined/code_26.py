import csv
import os

class CSVProcessor:
    """
    A class for processing CSV files, including reading, writing, and
    processing column data from CSV files.
    """

    def read_csv(self, file_name):
        """
        Read a CSV file and return the title and data.
        
        :param file_name: str, the name of the CSV file
        :return: tuple (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                title = next(reader)
                data = list(reader)
            return title, data
        except (FileNotFoundError, IOError):
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a CSV file.
        
        :param data: list of lists, the data to be written
        :param file_name: str, the name of the CSV file
        :return: int, 1 if success, 0 otherwise
        """
        if not data:
            return 0
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            return 1
        except (IOError, Exception):
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Process a CSV file to retain the N-th column of data capitalized,
        and save it to a new CSV file with '_process' suffix.
        
        :param N: int, the index of the column to process (0-based)
        :param save_file_name: str, the name of the file to be processed
        :return: int, 1 if success, 0 otherwise
        """
        title, data = self.read_csv(save_file_name)
        if not title or not data or N >= len(title):
            return 0

        new_data = [[row[N].upper()] for row in data]
        new_file_name = f"{os.path.splitext(save_file_name)[0]}_process.csv"
        
        if self.write_csv([title], new_file_name) and self.write_csv(new_data, new_file_name):
            return 1
        return 0