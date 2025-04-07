import csv

class CSVProcessor:
    """
    This class processes CSV files, including reading, writing, and specific operations,
    saving the results to a new CSV file.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Reads a CSV file and returns the header and data.

        Args:
            file_name (str): The name of the CSV file.

        Returns:
            tuple: A tuple containing the header (list) and data (list of lists).
                   Returns (None, None) if an error occurs.
        """
        try:
            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                data = list(reader)  # Read all rows into a list
                return header, data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return None, None
        except Exception as e:
            print(f"An error occurred while reading {file_name}: {e}")
            return None, None

    def write_csv(self, data, file_name):
        """
        Writes data to a CSV file.

        Args:
            data (list of lists): The data to write, including the header.
            file_name (str): The name of the CSV file to write to.

        Returns:
            bool: True if the write was successful, False otherwise.
        """
        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
            return True
        except Exception as e:
            print(f"An error occurred while writing to {file_name}: {e}")
            return False

    def process_csv_data(self, column_index, input_file_name, output_file_name=None):
        """
        Reads a CSV file, extracts a specific column, capitalizes the data,
        and writes the processed data to a new CSV file.

        Args:
            column_index (int): The index of the column to process (0-based).
            input_file_name (str): The name of the input CSV file.
            output_file_name (str, optional): The name of the output CSV file.
                                               If None, defaults to input_file_name_processed.csv

        Returns:
            bool: True if the processing and writing were successful, False otherwise.
        """
        header, data = self.read_csv(input_file_name)

        if header is None or data is None:
            return False

        processed_data = []
        for row in data:
            try:
                processed_data.append([row[column_index].upper()])  # Capitalize the value
            except IndexError:
                print(f"Warning: Column index {column_index} out of bounds for row: {row}")
                return False #Or continue if you want to skip the row: continue
            except Exception as e:
                print(f"An error occurred during processing: {e}")
                return False


        if output_file_name is None:
            output_file_name = input_file_name.replace(".csv", "_processed.csv") #more robust filename generation

        # Create the data structure needed for write_csv: header + processed data
        output_data = [header]
        for row in processed_data:
            output_data.append(row)

        # Write header and processed data to the output file
        if self.write_csv(output_data, output_file_name):
            return True
        else:
            return False

if __name__ == '__main__':
    # Example usage (create a dummy CSV for testing)
    test_data = [['a', 'b', 'c', 'd'], ['hElLo', 'YoU', 'ME', 'LoW'], ['another', 'row', 'data', 'here']]
    csv_processor = CSVProcessor()
    csv_processor.write_csv(test_data, 'read_test.csv')

    # Test the process_csv_data function
    if csv_processor.process_csv_data(0, 'read_test.csv'):
        print("Processing successful!")
    else:
        print("Processing failed.")

    # Verify the output
    title, data = csv_processor.read_csv('read_test_processed.csv')
    if title and data:
        print(f"Title: {title}")
        print(f"Data: {data}") # Expected output: [['HELLO'], ['ANOTHER']]
    else:
        print("Could not verify the output due to read error.")

    # Test write_csv function
    if csv_processor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv'):
        print("Write successful!")
    else:
        print("Write failed.")