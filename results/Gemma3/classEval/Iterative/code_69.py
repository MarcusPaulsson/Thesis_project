import PyPDF2
import os

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = []
        for fp in filepaths:
            try:
                self.readers.append(PyPDF2.PdfFileReader(fp))
            except FileNotFoundError:
                print(f"Error: File not found at {fp}")
            except Exception as e:
                print(f"Error opening {fp}: {e}")

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        """
        pdf_writer = PyPDF2.PdfFileWriter()
        for reader in self.readers:
            if reader:  # Check if the reader is valid
                for page in reader.pages:
                    pdf_writer.addPage(page)

        try:
            with open(output_filepath, 'wb') as output_file:
                pdf_writer.write(output_file)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            print(f"Error merging PDFs: {e}")
            return None

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        """
        pdf_texts = []
        for reader in self.readers:
            if reader:  # Check if the reader is valid
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                pdf_texts.append(text)
        return pdf_texts