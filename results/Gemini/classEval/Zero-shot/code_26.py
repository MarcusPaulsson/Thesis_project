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
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
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
            return None, None


    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in data:
                    writer.writerow(row)
            return 1
        except Exception as e:
            print(f"Error writing to file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
        title, data = self.read_csv(save_file_name)
        if title is None or data is None:
            return 0

        new_data = []
        for row in data:
            try:
                new_data.append([row[N].upper()])
            except IndexError:
                print(f"IndexError: Column {N} not found in row {row}")
                return 0

        new_file_name = save_file_name.replace(".csv", "_process.csv")
        
        data_to_write = [title, new_data[0]] if len(new_data) == 1 else [title] + new_data
        
        
        
        
        
        
        
        try:
            with open(new_file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(title)
                for row in new_data:
                    writer.writerow(row)

            return 1
        except Exception as e:
            print(f"Error writing to file: {e}")
            return 0