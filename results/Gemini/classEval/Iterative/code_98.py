import xml.etree.ElementTree as ET


class XMLProcessor:
    """
    A class for handling XML files, including reading, writing, processing, and finding elements.
    """

    def __init__(self, file_name):
        """
        Initializes the XMLProcessor object with the given file name.

        Args:
            file_name (str): The name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and sets the root element.

        Returns:
            ET.Element: The root element of the XML file, or None if an error occurred.
        """
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            print(f"Error: File '{self.file_name}' not found.")
            return None
        except ET.ParseError as e:
            print(f"Error: Failed to parse XML file '{self.file_name}': {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while reading '{self.file_name}': {e}")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.

        Args:
            file_name (str): The name of the file to write the XML data to.

        Returns:
            bool: True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to write.  Call read_xml() first.")
            return False

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name, encoding="utf-8", xml_declaration=True)  # Added encoding and declaration
            return True
        except Exception as e:
            print(f"Error writing to file '{file_name}': {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements by converting text to uppercase and writes the updated XML data to a new file.

        Args:
            file_name (str): The name of the file to write the modified XML data to.

        Returns:
            bool: True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: XML data not loaded. Call read_xml() first.")
            return False

        try:
            for element in self.root.iter():
                if element.text:
                    element.text = element.text.upper()
            return self.write_xml(file_name)
        except Exception as e:
            print(f"Error processing XML data: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds all XML elements with the specified name.

        Args:
            element_name (str): The name of the elements to find.

        Returns:
            list: A list of found elements with the specified name.  Returns an empty list if no elements are found or if the XML is not loaded.
        """
        if self.root is None:
            print("Error: XML data not loaded. Call read_xml() first.")
            return []

        try:
            return self.root.findall(element_name)
        except Exception as e:
            print(f"Error finding element '{element_name}': {e}")
            return []