import openpyxl
import os


class ExcelProcessor:
    """
    This is a class for processing excel files, including reading and writing excel data,
    as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Reads data from an Excel file.

        :param file_name: str, The name of the Excel file to read.
        :return: list of tuples, The data in the Excel file, or None if an error occurred.
        """
        if not file_name:
            print("Error: File name cannot be empty.")
            return None

        try:
            workbook = openpyxl.load_workbook(file_name)
            sheet = workbook.active
            data = []
            for row in sheet.rows:
                row_data = tuple(cell.value for cell in row)
                data.append(row_data)
            return data
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the Excel file: {e}")
            return None

    def write_excel(self, data, file_name):
        """
        Writes data to a specified Excel file.

        :param data: list of tuples, The data to be written.
        :param file_name: str, The name of the Excel file to write to.
        :return: bool, True if writing was successful, False otherwise.
        """
        if not file_name:
            print("Error: File name cannot be empty.")
            return False

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
        Processes Excel data by converting the specified column to uppercase and saving to a new file.

        :param column_index: int, The index of the column to convert to uppercase (0-based).
        :param file_name: str, The name of the source Excel file.
        :return: tuple (bool, str), A tuple containing:
                 - bool: True if processing and writing were successful, False otherwise.
                 - str: The name of the output file if successful, None otherwise.
        """
        if not isinstance(column_index, int):
            print("Error: Column index must be an integer.")
            return False, None

        if not file_name:
            print("Error: File name cannot be empty.")
            return False, None

        try:
            data = self.read_excel(file_name)
            if data is None:
                return False, None

            new_data = []
            for row in data:
                row_list = list(row)  # Convert tuple to list for modification
                if 0 <= column_index < len(row):
                    cell_value = row[column_index]
                    if cell_value is not None:
                        row_list.append(str(cell_value).upper())
                    else:
                        row_list.append(None)  # Handle None values appropriately
                else:
                    print(f"Error: Column index {column_index} is out of range.")
                    return False, None
                new_data.append(tuple(row_list))  # Convert back to tuple

            output_file_name = "processed_" + file_name
            write_success = self.write_excel(new_data, output_file_name)

            if write_success:
                return True, output_file_name
            else:
                return False, None

        except Exception as e:
            print(f"An error occurred while processing the Excel data: {e}")
            return False, None