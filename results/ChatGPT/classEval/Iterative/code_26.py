import csv
import os

class CSVProcessor:
    """
    This class processes CSV files, including reading, writing, and specific operations on CSV data.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Reads a CSV file and returns the title and data.
        :param file_name: str, name of the CSV file
        :return: (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, mode='r', newline='') as f:
                reader = csv.reader(f)
                title = next(reader)
                data = [row for row in reader]
            return title, data
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return [], []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Writes data into a CSV file.
        :param data: list of lists, data to write
        :param file_name: str, name of the CSV file
        :return: int, 1 if successful, 0 otherwise
        """
        try:
            with open(file_name, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            return 1
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Processes a CSV file to retain only the N-th column (0-indexed), capitalizes the data,
        and saves it into a new CSV file.
        :param N: int, the N-th column (0-indexed)
        :param save_file_name: str, the name of the file to be processed
        :return: int, 1 if successful, 0 otherwise
        """
        try:
            title, data = self.read_csv(save_file_name)
            if not title or not data:  # Check if read was successful
                return 0

            new_data = [[row[N].upper()] for row in data if len(row) > N]
            new_file_name = f"{os.path.splitext(save_file_name)[0]}_process.csv"
            self.write_csv([title], new_file_name)
            self.write_csv(new_data, new_file_name)
            return 1
        except IndexError:
            print(f"Column index {N} is out of range.")
            return 0
        except Exception as e:
            print(f"An error occurred during processing: {e}")
            return 0