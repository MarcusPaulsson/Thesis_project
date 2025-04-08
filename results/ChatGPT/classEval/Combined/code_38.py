import openpyxl


class ExcelProcessor:
    """
    A class to process Excel files, including reading, writing, and modifying Excel data.
    """

    def read_excel(self, file_name):
        """
        Reads data from an Excel file.
        
        :param file_name: str, the name of the Excel file to read.
        :return: list of tuples, data read from the Excel file or None if the file name is empty.
        """
        if not file_name:
            return None
        
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        return [row for row in sheet.iter_rows(values_only=True)]

    def write_excel(self, data, file_name):
        """
        Writes data to an Excel file.
        
        :param data: list of tuples, data to be written to the Excel file.
        :param file_name: str, the name of the Excel file to write to.
        :return: int, 1 for success, 0 for failure.
        """
        if not file_name:
            return 0
        
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(file_name)
        return 1

    def process_excel_data(self, column_index, source_file_name):
        """
        Modifies a specific column in the Excel file to be uppercase.
        
        :param column_index: int, the index of the column to modify (0-based).
        :param source_file_name: str, the name of the source Excel file.
        :return: tuple, (status code, output file name).
        """
        data = self.read_excel(source_file_name)
        
        if data is None or column_index >= len(data[0]):
            return 0, ""
        
        processed_data = []
        for i, row in enumerate(data):
            processed_row = list(row)
            if i == 0:
                processed_row.append(row[column_index].upper())  # Add header
            else:
                processed_row.append(row[column_index])  # Retain original value
            processed_data.append(tuple(processed_row))

        output_file_name = f"processed_{source_file_name}"
        success = self.write_excel(processed_data, output_file_name)
        return success, output_file_name