import PyPDF2
import os

from reportlab.pdfgen import canvas

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of file paths and creates PdfFileReader objects for each file.
        :param filepaths: list of str, paths to the PDF files
        """
        self.filepaths = filepaths
        self.readers = [self._open_pdf(fp) for fp in filepaths]

    @staticmethod
    def _open_pdf(filepath):
        """Open a PDF file and return a PdfFileReader object."""
        return PyPDF2.PdfFileReader(open(filepath, 'rb'))

    def merge_pdfs(self, output_filepath):
        """
        Merge the PDFs stored in self.readers into a single PDF and save to disk.
        
        :param output_filepath: str, output file path to save to
        :return: str, confirmation message
        """
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            merger.append(reader)

        with open(output_filepath, 'wb') as output_file:
            merger.write(output_file)

        merger.close()
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from PDF files in self.readers.
        
        :return: list of str, each element is the text of one PDF file
        """
        pdf_texts = []
        for reader in self.readers:
            text = ""
            for page in range(reader.getNumPages()):
                text += reader.getPage(page).extract_text() + "\n"
            pdf_texts.append(text)
        return pdf_texts

