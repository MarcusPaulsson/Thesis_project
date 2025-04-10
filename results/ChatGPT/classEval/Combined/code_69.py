import os
import unittest
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