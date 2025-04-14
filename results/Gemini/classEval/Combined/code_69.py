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
        for fp in self.filepaths:
            try:
                reader = PyPDF2.PdfFileReader(fp)
                self.readers.append(reader)
            except FileNotFoundError:
                print(f"Error: File not found at {fp}")
                self.readers.append(None)
            except PyPDF2.utils.PdfReadError:
                print(f"Error: Could not open or read PDF file at {fp}.  It may be encrypted or not a valid PDF.")
                self.readers.append(None)
            except Exception as e:
                print(f"Error reading {fp}: {e}")
                self.readers.append(None)

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.

        Args:
            output_filepath: The path to the output PDF file.

        Returns:
            A string indicating the success or failure of the merge operation.
        """
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            if reader:
                try:
                    merger.append(reader)
                except Exception as e:
                    return f"Error appending PDF: {e}"

        try:
            merger.write(output_filepath)
            merger.close()
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"Error writing merged PDF: {e}"

    def extract_text_from_pdfs(self):
        """
        Extracts text from multiple PDF files.

        Returns:
            A list of strings, where each string contains the extracted text from a PDF file.
            If a PDF file could not be read, an empty string is returned for that file.
        """
        pdf_texts = []
        for reader in self.readers:
            if reader:
                text = ""
                try:
                    for page_num in range(reader.numPages):
                        page = reader.getPage(page_num)
                        text += page.extractText()
                except Exception as e:
                    print(f"Error extracting text: {e}")
                    text = ""  # Ensure empty string is appended even if extraction fails
                pdf_texts.append(text)
            else:
                pdf_texts.append("")
        return pdf_texts