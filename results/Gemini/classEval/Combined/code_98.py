import xml.etree.ElementTree as ET


class XMLProcessor:
    """
    This is a class as XML files handler, including reading, writing, processing as well as finding elements in a XML file.
    """

    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        :param file_name:string, the name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file, or None if an error occurs.
        """
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            print(f"Error: File not found: {self.file_name}")
            return None
        except ET.ParseError:
            print(f"Error: XML parsing error in: {self.file_name}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to write.  Ensure XML has been read first.")
            return False

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing to file {file_name}: {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        Specifically, converts the text of all 'item' elements to uppercase.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to process. Ensure XML has been read first.")
            return False

        try:
            for element in self.root.findall('.//item'):
                if element.text is not None:
                    element.text = element.text.upper()

            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error processing and writing to file {file_name}: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.  Returns an empty list if no elements are found or if an error occurs.
        """
        if self.root is None:
            print("Error: No XML data to search. Ensure XML has been read first.")
            return []

        try:
            return self.root.findall(element_name)
        except Exception as e:
            print(f"Error finding elements with name {element_name}: {e}")
            return []