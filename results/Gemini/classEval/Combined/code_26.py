import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data, as well as processing specific operations and saving as a new CSV file.
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
            with open(file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                title = next(reader)
                data = list(reader)  # Read all rows into a list
                return title, data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return [], []
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :param data: list of lists, the data to write to the CSV file
        :return: int, if success return 1, or 0 otherwise
        """
        if not data or not file_name:
            return 0

        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)  # Use writerows to write all rows
            return 1
        except Exception as e:
            print(f"Error writing to CSV file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name: str, the name of file that needs to be processed.
        :return: int, if success return 1, or 0 otherwise
        """
        try:
            title, data = self.read_csv(save_file_name)
            if not title or not data:
                return 0

            processed_data = [[row[N].upper()] for row in data if len(row) > N]

            new_file_name = save_file_name.replace(".csv", "_process.csv")

            with open(new_file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(title)
                writer.writerows(processed_data)  # Use writerows to write all processed rows
            return 1
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return 0