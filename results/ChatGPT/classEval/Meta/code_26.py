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
        with open(file_name, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            title = next(reader)
            data = [row for row in reader]
        return title, data

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            return 1
        except Exception as e:
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name: the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        """
        title, data = self.read_csv(save_file_name)
        new_data = [[row[N].upper()] for row in data if len(row) > N]
        new_file_name = save_file_name[:-4] + '_process.csv'
        success = self.write_csv([title] + new_data, new_file_name)
        return success