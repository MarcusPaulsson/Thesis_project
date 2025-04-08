import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of filepaths.

        Args:
            filepaths (list[str]): A list of paths to PDF files.
        """
        self.filepaths = filepaths
        self.readers = []
        for fp in filepaths:
            try:
                reader = PyPDF2.PdfFileReader(fp)
                self.readers.append(reader)
            except FileNotFoundError:
                print(f"File not found: {fp}")
            except Exception as e:
                print(f"Error reading {fp}: {e}")

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.

        Args:
            output_filepath (str): The path to save the merged PDF file.

        Returns:
            str: A message indicating success or failure.
        """
        merger = PyPDF2.PdfFileMerger()
        try:
            for reader in self.readers:
                merger.append(reader)
            merger.write(output_filepath)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"Error merging PDFs: {e}"
        finally:
            merger.close()

    def extract_text_from_pdfs(self):
        """
        Extracts text from multiple PDF files.

        Returns:
            list[str]: A list of strings, where each string is the text extracted from a PDF file.
        """
        pdf_texts = []
        for reader in self.readers:
            text = ""
            try:
                for page_num in range(reader.getNumPages()):
                    page = reader.getPage(page_num)
                    text += page.extractText()
            except Exception as e:
                print(f"Error extracting text: {e}")
                text = ""  # or handle the error as appropriate
            pdf_texts.append(text)
        return pdf_texts