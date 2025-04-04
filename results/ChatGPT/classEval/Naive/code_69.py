import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using the PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of file paths.
        :param filepaths: List of strings representing the paths to PDF files.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF and saves it to the specified output file path.
        :param output_filepath: str, output file path to save the merged PDF.
        :return: str, confirmation message upon successful merge.
        """
        merger = PyPDF2.PdfWriter()
        for reader in self.readers:
            for page in reader.pages:
                merger.add_page(page)

        with open(output_filepath, 'wb') as output_file:
            merger.write(output_file)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extracts text from each PDF file and returns it as a list of strings.
        :return: list of str, each element is the text of one PDF file.
        """
        pdf_texts = []
        for reader in self.readers:
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            pdf_texts.append(text.strip())
        return pdf_texts