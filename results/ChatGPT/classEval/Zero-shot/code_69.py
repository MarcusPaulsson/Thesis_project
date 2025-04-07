import PyPDF2

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
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, output file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        """
        pdf_writer = PyPDF2.PdfFileWriter()

        for reader in self.readers:
            for page in range(reader.getNumPages()):
                pdf_writer.addPage(reader.getPage(page))

        with open(output_filepath, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        """
        pdf_texts = []
        for reader in self.readers:
            text = ''
            for page in range(reader.getNumPages()):
                text += reader.getPage(page).extractText()
            pdf_texts.append(text)
        return pdf_texts