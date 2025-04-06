import PyPDF2
from typing import List

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths: List[str]):
        """
        Initializes PDFHandler with a list of file paths.
        Creates a list of PdfReader objects for the provided file paths.
        
        :param filepaths: List of PDF file paths to be handled.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath: str) -> str:
        """
        Merges multiple PDF files into one and saves it to disk.
        
        :param output_filepath: str, output file path to save the merged PDF
        :return: str, message indicating the location of the saved merged PDF
        """
        writer = PyPDF2.PdfWriter()

        for reader in self.readers:
            for page in reader.pages:
                writer.add_page(page)

        with open(output_filepath, 'wb') as out_file:
            writer.write(out_file)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self) -> List[str]:
        """
        Extracts text from each PDF file and returns a list of text content.
        
        :return: List of strings, each containing the text of one PDF file
        """
        pdf_texts = []
        
        for reader in self.readers:
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text extraction is successful
                    text += page_text
            pdf_texts.append(text)

        return pdf_texts