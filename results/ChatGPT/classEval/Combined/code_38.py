import openpyxl
from typing import List, Tuple, Optional


class ExcelProcessor:
    """
    A class for processing Excel files, including reading and writing data,
    and performing specific operations before saving as a new Excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name: str) -> Optional[List[Tuple]]:
        """
        Reads data from an Excel file.
        
        :param file_name: str, Excel file name to read
        :return: list of tuples, Data in Excel
        """
        if not file_name:
            return None
        
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        return [tuple(row) for row in sheet.iter_rows(values_only=True)]

    def write_excel(self, data: List[Tuple], file_name: str) -> int:
        """
        Writes data to the specified Excel file.
        
        :param data: list of tuples, Data to be written
        :param file_name: str, Excel file name to write to
        :return: int, 1 if writing was successful, 0 otherwise
        """
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            
            for row in data:
                sheet.append(row)
                
            workbook.save(file_name)
            return 1
        except Exception:
            return 0

    def process_excel_data(self, column_index: int, file_name: str) -> Tuple[int, str]:
        """
        Changes the specified column in the Excel file to uppercase.
        
        :param column_index: int, The index of the column to change
        :param file_name: str, Source file name
        :return: Tuple[int, str], Return value of write_excel and the saved file name of the processed data
        """
        data = self.read_excel(file_name)
        
        if data is None or column_index < 0 or column_index >= len(data[0]):
            return 0, ''
        
        processed_data = []
        header = list(data[0]) + [data[0][column_index].upper()]
        processed_data.append(tuple(header))
        
        for row in data[1:]:
            new_row = list(row) + [row[column_index]]
            processed_data.append(tuple(new_row))
        
        output_file_name = f"processed_{file_name}"
        success = self.write_excel(processed_data, output_file_name)
        
        return success, output_file_name