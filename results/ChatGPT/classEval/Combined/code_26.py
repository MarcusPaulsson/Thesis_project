import csv
import os


class CSVProcessor:
    """
    A class for processing CSV files, including reading and writing CSV data,
    as well as processing specific operations and saving as a new CSV file.
    """

    def read_csv(self, file_name):
        """
        Read the CSV file by file_name, get the title and data from it.
        
        :param file_name: str, name of the CSV file
        :return: (list, list), first row is title, the rest is data
        """
        with open(file_name, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            title = next(reader)
            data = [row for row in reader]
        return title, data

    def write_csv(self, data, file_name):
        """
        Write data into a CSV file.
        
        :param data: list, list of lists containing data to write
        :param file_name: str, name of the CSV file
        :return: int, 1 if success, 0 otherwise
        """
        if not data or not file_name:
            return 0
        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        return 1

    def process_csv_data(self, column_index, input_file_name):
        """
        Read a CSV file, retain only the specified column, capitalize the data,
        and save it to a new CSV file with '_process' suffix.
        
        :param column_index: int, the column index to be processed (0-based)
        :param input_file_name: str, the name of the file to be processed
        :return: int, 1 if success, 0 otherwise
        """
        try:
            title, data = self.read_csv(input_file_name)
            new_data = [[row[column_index].upper()] for row in data if len(row) > column_index]
            new_file_name = f"{os.path.splitext(input_file_name)[0]}_process.csv"
            success = self.write_csv([title], new_file_name) and self.write_csv(new_data, new_file_name)
            return 1 if success else 0
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return 0