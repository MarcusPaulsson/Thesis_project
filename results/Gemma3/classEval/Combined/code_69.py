import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of file paths.

        :param filepaths: A list of strings, where each string is a path to a PDF file.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfFileReader(open(fp, 'rb')) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.

        :param output_filepath: The path to save the merged PDF file.
        :return: A string indicating the success of the merge operation.
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
        Extracts text from each PDF file in the list of file paths.

        :return: A list of strings, where each string is the text content of a PDF file.
        """
        pdf_texts = []
        for reader in self.readers:
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            pdf_texts.append(text)
        return pdf_texts