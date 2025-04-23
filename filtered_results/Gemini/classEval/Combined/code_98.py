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
            Element: The root element of the XML file, or None if an error occurred.
        """
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            print(f"Error: XML file '{self.file_name}' not found.")
            return None
        except ET.ParseError:
            print(f"Error: Failed to parse XML file '{self.file_name}'.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
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
            print("Error: No XML data to write. Please read an XML file first.")
            return False

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing to file '{file_name}': {e}")
            return False

    def process_xml_data(self, file_name, element_name='item'):
        """
        Modifies the text data of specified XML elements to uppercase and writes the updated XML data to a new file.

        Args:
            file_name (str): The name of the file to write the modified XML data to.
            element_name (str): The name of the elements to process (default: 'item').

        Returns:
            bool: True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to process. Please read an XML file first.")
            return False

        try:
            for element in self.root.findall(element_name):
                if element.text:  # Check if the element has text before processing
                    element.text = element.text.upper()

            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True

        except Exception as e:
            print(f"Error processing and writing to file '{file_name}': {e}")
            return False

    def find_element(self, element_name):
        """
        Finds all XML elements with the specified name.

        Args:
            element_name (str): The name of the elements to find.

        Returns:
            list: A list of found elements with the specified name.  Returns an empty list if no elements are found or if an error occurs.
        """
        if self.root is None:
            print("Error: No XML data to search. Please read an XML file first.")
            return []

        try:
            elements = self.root.findall(element_name)
            return elements
        except Exception as e:
            print(f"Error finding elements with name '{element_name}': {e}")
            return []