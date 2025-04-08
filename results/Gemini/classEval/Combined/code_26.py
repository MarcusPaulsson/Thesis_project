import csv

class CSVProcessor:
    """
    A class for processing CSV files, including reading, writing, and specific data transformations.
    """

    def read_csv(self, file_name):
        """
        Reads a CSV file and returns the header and data rows.

        Args:
            file_name (str): The name of the CSV file to read.

        Returns:
            tuple: A tuple containing the header (list of strings) and data (list of lists).
                   Returns empty lists if the file is not found or an error occurs.
        """
        try:
            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                data = list(reader)  # Read all rows into a list
                return header, data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return [], []
        except Exception as e:
            print(f"An error occurred: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Writes data to a CSV file.

        Args:
            data (list of lists): The data to write, where the first sublist is the header.
            file_name (str): The name of the CSV file to write to.

        Returns:
            int: 1 if the write was successful, 0 otherwise.
        """
        if not data:
            print("Warning: No data to write.")
            return 0

        try:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data[0])  # Write the header
                writer.writerows(data[1:]) # Write the data rows
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def process_csv_data(self, column_index, input_file_name):
        """
        Reads a CSV file, extracts a specific column, converts it to uppercase,
        and writes the processed data to a new CSV file.

        Args:
            column_index (int): The index of the column to extract and process (0-based).
            input_file_name (str): The name of the input CSV file.

        Returns:
            int: 1 if the processing and writing were successful, 0 otherwise.
        """
        try:
            header, data = self.read_csv(input_file_name)
            if not header or not data:
                print("Error: Could not read data from the input file.")
                return 0

            processed_data = []
            for row in data:
                if len(row) > column_index:
                    processed_data.append([row[column_index].upper()])
                else:
                    print(f"Warning: Row {row} does not have enough columns. Skipping row.")
                    return 0 #Return 0 if any row does not have enough columns

            output_file_name = input_file_name.replace(".csv", "_process.csv")
            
            # Write the processed data to the new CSV file
            data_to_write = [header]  # Use original header
            data_to_write.extend(processed_data)

            return self.write_csv(data_to_write, output_file_name)

        except Exception as e:
            print(f"An error occurred during processing: {e}")
            return 0