import csv

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
                title = next(reader)  # Get the first row as the title
                data = list(reader)  # Get the rest of the rows as data
                return title, data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return None, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
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
        title, data = self.read_csv(save_file_name)
        if title is None or data is None:
            return 0

        processed_data = []
        for row in data:
            try:
                processed_data.append([row[N].upper()])
            except IndexError:
                print(f"Error: Column {N} does not exist in row: {row}")
                return 0
            except Exception as e:
                print(f"An error occurred: {e}")
                return 0

        new_file_name = save_file_name.replace(".csv", "_process.csv") if ".csv" in save_file_name else save_file_name + "_process.csv"

        try:
            with open(new_file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(title)  # Write the original title
                writer.writerows(processed_data)
            return 1
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")
            return 0

if __name__ == '__main__':
    # Example Usage (Create read_test.csv for testing)
    with open('read_test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c', 'd'])
        writer.writerow(['hElLo', 'YoU', 'ME', 'LoW'])

    csvProcessor = CSVProcessor()
    print(csvProcessor.read_csv('read_test.csv'))
    print(csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv'))
    print(csvProcessor.process_csv_data(0, 'read_test.csv'))
    print(csvProcessor.read_csv('read_test_process.csv'))