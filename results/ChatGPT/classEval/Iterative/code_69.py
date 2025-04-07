import PyPDF2
import os

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Takes a list of file paths (filepaths) as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [self._open_pdf(fp) for fp in filepaths]

    def _open_pdf(self, filepath):
        """
        Helper method to open a PDF file and return a PdfFileReader object.
        :param filepath: str, path to the PDF file
        :return: PdfFileReader object
        """
        try:
            return PyPDF2.PdfReader(filepath)
        except Exception as e:
            raise ValueError(f"Error opening {filepath}: {e}")

    def merge_pdfs(self, output_filepath):
        """
        Merge PDF files in self.readers to one pdf and save it to disk.
        :param output_filepath: str, output file path to save to
        :return: str, confirmation message if successfully merged
        """
        pdf_writer = PyPDF2.PdfWriter()
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                pdf_writer.add_page(reader.pages[page_num])
        
        with open(output_filepath, 'wb') as out_file:
            pdf_writer.write(out_file)
        
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from PDF files in self.readers.
        :return: list of str, each element is the text of one PDF file
        """
        pdf_texts = []
        for reader in self.readers:
            text = ''
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text() or ''
            pdf_texts.append(text)
        return pdf_texts