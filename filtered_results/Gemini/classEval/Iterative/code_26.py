import csv
import os

class CSVProcessor:
    """
    This is a class for processing CSV files, including readring and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                title = next(reader)
                data = []
                for row in reader:
                    data.append(row)
                return title, data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return [], []
        except Exception as e:
            print(f"An error occurred: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        if not data or not isinstance(data, list) or len(data) < 1:
            return 0

        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data[0])
                for row in data[1:]:
                    writer.writerow(row)
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            title, data = self.read_csv(save_file_name)
            if not title or not data:
                return 0

            new_data = []
            for row in data:
                try:
                    new_data.append([row[N].upper()])
                except IndexError:
                    print(f"Index {N} out of range for row: {row}")
                    return 0

            new_file_name = save_file_name.replace(".csv", "_process.csv")
            
            processed_data = [title] + new_data
            return self.write_csv(processed_data, new_file_name)
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0