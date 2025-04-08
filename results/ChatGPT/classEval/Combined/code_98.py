import xml.etree.ElementTree as ET
import os


class XMLProcessor:
    """
    A class to handle XML files, including reading, writing, processing, and finding elements in an XML file.
    """

    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        :param file_name: str, the name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file or None if the file name is empty.
        """
        if not self.file_name:
            return None
        
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except (ET.ParseError, FileNotFoundError):
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: str, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if not file_name or self.root is None:
            return False
        
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception:
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: str, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if not file_name or self.root is None:
            return False
        
        for item in self.root.findall('item'):
            item.text = item.text.upper()

        return self.write_xml(file_name)

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: str, the name of the elements to find.
        :return: list, a list of found elements with the specified name or an empty list if root is None.
        """
        if self.root is None:
            return []
        
        return self.root.findall(element_name)