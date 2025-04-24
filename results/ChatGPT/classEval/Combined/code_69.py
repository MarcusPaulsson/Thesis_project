import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of file paths.
        :param filepaths: list of str, paths to PDF files
        """
        self.filepaths = filepaths
        self.readers = self._initialize_readers(filepaths)

    def _initialize_readers(self, filepaths):
        """
        Creates a list of PdfFileReader objects for each file.
        :param filepaths: list of str, paths to PDF files
        :return: list of PdfFileReader objects
        """
        readers = []
        for fp in filepaths:
            try:
                reader = PyPDF2.PdfFileReader(fp)
                readers.append(reader)
            except Exception as e:
                print(f"Error reading {fp}: {e}")
        return readers

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.
        :param output_filepath: str, output file path to save the merged PDF
        :return: str, confirmation message if successfully merged
        """
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            merger.append(reader)
        merger.write(output_filepath)
        merger.close()
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extracts text from each PDF file.
        :return: list of str, each element is the text of one PDF file
        """
        pdf_texts = []
        for reader in self.readers:
            text = self._extract_text_from_reader(reader)
            pdf_texts.append(text)
        return pdf_texts

    def _extract_text_from_reader(self, reader):
        """
        Extracts text from a single PdfFileReader object.
        :param reader: PdfFileReader object
        :return: str, extracted text
        """
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text