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
        self.readers = []
        for filepath in filepaths:
            try:
                self.readers.append(PyPDF2.PdfFileReader(filepath))
            except FileNotFoundError:
                print(f"Error: File not found: {filepath}")
                self.readers.append(None)  # Append None to maintain list length
            except Exception as e:
                print(f"Error opening {filepath}: {e}")
                self.readers.append(None)

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        merger = PyPDF2.PdfFileMerger()
        
        for reader in self.readers:
            if reader:  # Check if the reader is valid (not None)
                try:
                    merger.append(reader)
                except Exception as e:
                    print(f"Error appending PDF: {e}")
            else:
                print("Skipping invalid PDF file.")

        try:
            merger.write(output_filepath)
            merger.close()
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            print(f"Error writing merged PDF: {e}")
            return None  # Or raise the exception if appropriate


    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        pdf_texts = []
        for reader in self.readers:
            if reader:
                text = ""
                try:
                    for page_num in range(reader.numPages):
                        page = reader.getPage(page_num)
                        text += page.extractText()
                    pdf_texts.append(text)
                except Exception as e:
                    print(f"Error extracting text: {e}")
                    pdf_texts.append(None) # Handle extraction errors.
            else:
                pdf_texts.append(None) #Handle invalid readers
        return pdf_texts