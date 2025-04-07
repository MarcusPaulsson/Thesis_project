import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        If a file is not found or cannot be read, a None is appended to the readers list.
        """
        self.filepaths = filepaths
        self.readers = []
        for fp in filepaths:
            try:
                with open(fp, 'rb') as f:
                    self.readers.append(PyPDF2.PdfFileReader(f))
            except FileNotFoundError:
                print(f"File not found: {fp}")
                self.readers.append(None)
            except PyPDF2.utils.PdfReadError:
                print(f"Could not read PDF: {fp}")
                self.readers.append(None)
            except Exception as e:
                print(f"Error opening {fp}: {e}")
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
            if reader:
                try:
                    merger.append(reader)
                except Exception as e:
                    print(f"Error appending PDF: {e}")

        try:
            with open(output_filepath, 'wb') as output_file:
                merger.write(output_file)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"Error merging PDFs: {e}"
        finally:
            merger.close()


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
                    for page_num in range(reader.getNumPages()):
                        page = reader.getPage(page_num)
                        text += page.extractText()
                except Exception as e:
                    print(f"Error extracting text: {e}")
                    text = "" # Ensure an empty string is added even if extraction fails
                pdf_texts.append(text)
            else:
                pdf_texts.append("")
        return pdf_texts