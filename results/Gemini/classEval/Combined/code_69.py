import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of filepaths.

        Args:
            filepaths: A list of strings, where each string is a path to a PDF file.
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
                print(f"Error opening {fp}: {e}")

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.

        Args:
            output_filepath: The path to the output PDF file.

        Returns:
            A string indicating the success of the merge operation.
        """
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            try:
                merger.append(reader)
            except Exception as e:
                print(f"Error appending PDF: {e}")
                return f"Error merging PDFs."

        try:
            merger.write(output_filepath)
        except Exception as e:
            print(f"Error writing merged PDF: {e}")
            return f"Error saving merged PDF."
        finally:
            merger.close()

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extracts text from multiple PDF files.

        Returns:
            A list of strings, where each string is the extracted text from a PDF file.
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