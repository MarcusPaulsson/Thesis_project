import openpyxl


class ExcelProcessor:
    """
    A class for processing Excel files, including reading, writing, and modifying Excel data.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Read data from an Excel file.
        
        :param file_name: str, path to the Excel file to read.
        :return: list of tuples, data from the Excel file.
        """
        try:
            wb = openpyxl.load_workbook(file_name)
            sheet = wb.active
            data = [row for row in sheet.iter_rows(values_only=True)]
            return data
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    def write_excel(self, data, file_name):
        """
        Write data to an Excel file.
        
        :param data: list of tuples, data to write to the Excel file.
        :param file_name: str, path to the Excel file to write to.
        :return: bool, True if writing was successful, False otherwise.
        """
        try:
            wb = openpyxl.Workbook()
            sheet = wb.active
            for row in data:
                sheet.append(row)
            wb.save(file_name)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def process_excel_data(self, N, source_file_name):
        """
        Modify a specified column in the Excel file to uppercase.
        
        :param N: int, the index of the column to change (0-based).
        :param source_file_name: str, path to the source Excel file.
        :return: (bool, str), True if processing was successful, along with the name of the saved file.
        """
        data = self.read_excel(source_file_name)
        if not data:
            return False, source_file_name
        
        modified_data = []
        for row in data:
            modified_row = list(row)
            if N < len(modified_row):
                modified_row[N] = str(modified_row[N]).upper()
            modified_data.append(tuple(modified_row))
        
        output_file_name = f"processed_{source_file_name}"
        success = self.write_excel(modified_data, output_file_name)
        return success, output_file_name