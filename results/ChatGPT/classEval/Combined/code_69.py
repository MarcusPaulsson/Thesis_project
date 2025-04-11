import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initialize PDFHandler with a list of file paths.
        """
        self.filepaths = filepaths
        self.readers = [PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Merge multiple PDF files into a single PDF file.
        :param output_filepath: str, output file path to save to
        :return: str, confirmation message if successfully merged
        """
        pdf_writer = PdfWriter()

        for reader in self.readers:
            for page in reader.pages:
                pdf_writer.add_page(page)

        with open(output_filepath, 'wb') as output_file:
            pdf_writer.write(output_file)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from PDF files.
        :return: list of str, each element is the text of one PDF file
        """
        pdf_texts = []

        for reader in self.readers:
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            pdf_texts.append(text + "\n")

        return pdf_texts

