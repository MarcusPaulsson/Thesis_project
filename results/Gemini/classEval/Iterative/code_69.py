import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        Initializes the PDFHandler with a list of filepaths.
        Opens each PDF file and creates a PdfFileReader object. Handles potential FileNotFoundError and generic Exceptions.
        """
        self.filepaths = filepaths
        self.readers = []
        for fp in filepaths:
            try:
                with open(fp, 'rb') as f:  # Open in binary mode
                    self.readers.append(PyPDF2.PdfFileReader(f))
            except FileNotFoundError:
                print(f"Error: File not found - {fp}")
                self.readers.append(None)  # Append None to maintain the list length
            except Exception as e:
                print(f"Error opening {fp}: {e}")
                self.readers.append(None)

    def merge_pdfs(self, output_filepath):
        """
        Merges multiple PDF files into a single PDF file.

        Args:
            output_filepath (str): The file path for the merged PDF.

        Returns:
            str: A message indicating the successful merging and the output file path, or None if merging fails.
        """
        merger = PyPDF2.PdfFileMerger()
        try:
            for reader in self.readers:
                if reader:  # Check if the reader is valid (not None)
                    merger.append(reader)
            with open(output_filepath, 'wb') as output_file:
                merger.write(output_file)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            print(f"Error during merge: {e}")
            return None
        finally:
            merger.close()

    def extract_text_from_pdfs(self):
        """
        Extracts text from each PDF file.

        Returns:
            list: A list of strings, where each string contains the extracted text from a PDF file.
                  Returns an empty string for invalid PDF files.
        """
        pdf_texts = []
        for reader in self.readers:
            if reader:  # Check if the reader is valid (not None)
                text = ""
                try:
                    for page_num in range(reader.getNumPages()):
                        page = reader.getPage(page_num)
                        text += page.extractText()
                except Exception as e:
                    print(f"Error extracting text: {e}")
                    text = ""  # Return empty string if extraction fails
                pdf_texts.append(text)
            else:
                pdf_texts.append("")  # Append an empty string for invalid readers
        return pdf_texts

if __name__ == '__main__':
    # Create dummy PDF files for testing
    # Note: These are NOT actual PDF files, but text files. Real PDF files are needed for proper functionality.
    with open("a.pdf", "w") as f:
        f.write("Test a.pdf")
    with open("b.pdf", "w") as f:
        f.write("Test b.pdf")

    handler = PDFHandler(['a.pdf', 'b.pdf'])
    print(handler.extract_text_from_pdfs())
    print(handler.merge_pdfs('out.pdf'))