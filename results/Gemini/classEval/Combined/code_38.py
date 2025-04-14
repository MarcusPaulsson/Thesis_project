import openpyxl


class ExcelProcessor:
    """
    This is a class for processing excel files, including reading and writing excel data, as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        try:
            workbook = openpyxl.load_workbook(file_name)
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows():
                row_data = tuple(cell.value for cell in row)
                data.append(row_data)
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            return None
        except openpyxl.utils.exceptions.InvalidFileException:
            print(f"Error: File '{file_name}' is not a valid Excel file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 1 for successful writing, 0 for failed writing
        """
        if not file_name:
            print("Error: File name cannot be empty.")
            return 0

        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row_data in data:
                sheet.append(row_data)
            workbook.save(file_name)
            return 1
        except Exception as e:
            print(f"An error occurred while writing to Excel: {e}")
            return 0

    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        """
        data = self.read_excel(save_file_name)
        if data is None:
            return 0, None

        if not data:
            print("Error: The Excel file is empty.")
            return 0, None

        new_data = []
        for row in data:
            new_row = list(row)
            if 0 <= N < len(new_row):
                original_value = new_row[N]
                if isinstance(original_value, str):
                    new_row.append(original_value.upper())
                else:
                    new_row.append(original_value)
            else:
                print(f"Error: Column index {N} is out of range.")
                return 0, None
            new_data.append(tuple(new_row))

        output_file_name = "processed_" + save_file_name
        write_result = self.write_excel(new_data, output_file_name)
        return write_result, output_file_name