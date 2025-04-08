import PyPDF2
import os
import unittest
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


class TestPDFHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_files = ["test1.pdf", "test2.pdf"]
        cls.test_text = ["This is a test1.", "This is a test2."]
        for i, text in enumerate(cls.test_text):
            c = canvas.Canvas(cls.test_files[i])
            c.drawString(100, 100, text)
            c.showPage()
            c.save()

    @classmethod
    def tearDownClass(cls):
        for filename in cls.test_files:
            os.remove(filename)
        if os.path.exists("merged.pdf"):
            os.remove("merged.pdf")

    def test_merge_pdfs(self):
        handler = PDFHandler(self.test_files)
        result = handler.merge_pdfs("merged.pdf")
        self.assertEqual("Merged PDFs saved at merged.pdf", result)
        self.assertTrue(os.path.exists("merged.pdf"))

    def test_extract_text_from_pdfs(self):
        handler = PDFHandler(self.test_files)
        result = handler.extract_text_from_pdfs()
        self.assertEqual(result, ["This is a test1.\n", "This is a test2.\n"])

    def test_main(self):
        handler = PDFHandler(self.test_files)
        merge_result = handler.merge_pdfs("merged.pdf")
        self.assertEqual("Merged PDFs saved at merged.pdf", merge_result)
        self.assertTrue(os.path.exists("merged.pdf"))

        extract_result = handler.extract_text_from_pdfs()
        self.assertEqual(extract_result, ["This is a test1.\n", "This is a test2.\n"])