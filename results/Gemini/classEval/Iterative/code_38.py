import openpyxl
from openpyxl.utils.exceptions import InvalidFileException


class ExcelProcessor:
    """
    A class for processing Excel files, including reading and writing data,
    performing specific operations, and saving to a new Excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Reads data from an Excel file.

        Args:
            file_name (str): The name of the Excel file to read.

        Returns:
            list: A list of tuples, where each tuple represents a row of data.
                  Returns None if the file is not found or an error occurs.
        """
        try:
            workbook = openpyxl.load_workbook(file_name)
            sheet = workbook.active
            data = list(sheet.iter_rows(values_only=True))  # Directly convert to list
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return None
        except InvalidFileException:
            print(f"Error: File '{file_name}' is not a valid Excel file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while reading the Excel file: {e}")
            return None

    def write_excel(self, data, file_name):
        """
        Writes data to an Excel file.

        Args:
            data (list): A list of tuples or lists, where each item represents a row to be written.
            file_name (str): The name of the Excel file to write to.

        Returns:
            bool: True if the data was written successfully, False otherwise.
        """
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row_data in data:
                sheet.append(row_data)
            workbook.save(file_name)
            return True
        except Exception as e:
            print(f"An error occurred while writing to the Excel file: {e}")
            return False

    def process_excel_data(self, column_index, file_name):
        """
        Processes data in an Excel file by converting the specified column to uppercase.

        Args:
            column_index (int): The index of the column to convert to uppercase (0-based).
            file_name (str): The name of the Excel file to process.

        Returns:
            tuple: A tuple containing a boolean indicating success (True/False) and the output file name.
                   Returns (False, None) if an error occurs.
        """
        try:
            data = self.read_excel(file_name)
            if data is None:
                return False, None

            new_data = []
            for row in data:
                row_list = list(row)  # Convert tuple to list for modification
                if 0 <= column_index < len(row_list):  # Check if column_index is valid
                    cell_value = row_list[column_index]
                    if isinstance(cell_value, (int, float)):
                        row_list[column_index] = str(cell_value).upper()
                    elif isinstance(cell_value, str):
                        row_list[column_index] = cell_value.upper()
                new_data.append(tuple(row_list))  # Convert back to tuple

            output_file_name = "processed_" + file_name
            success = self.write_excel(new_data, output_file_name)
            return success, output_file_name
        except Exception as e:
            print(f"An error occurred while processing the Excel data: {e}")
            return False, None


if __name__ == '__main__':
    processor = ExcelProcessor()

    # Example Usage for write_excel
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia'),
        ('Julia', 28, 'Germany')
    ]
    write_status = processor.write_excel(new_data, 'test_data.xlsx')
    print(f"Write Status: {write_status}")

    # Example Usage for process_excel_data
    success, output_file = processor.process_excel_data(0, 'test_data.xlsx')  # Change the first column to uppercase
    print(f"Process Status: {success}, Output File: {output_file}")

    # Example Usage for read_excel:
    read_data = processor.read_excel('test_data.xlsx')
    if read_data:
        print("Read Data:")
        for row in read_data:
            print(row)