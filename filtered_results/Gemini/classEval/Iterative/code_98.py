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
        :return: Element, the root element of the XML file.
        """
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            return None
        except ET.ParseError:
            return None
        except Exception:
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            return False
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except FileNotFoundError:
            return False
        except Exception:
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            return False
        try:
            for item in self.root.findall('item'):
                if item.text:
                    item.text = item.text.upper()
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except FileNotFoundError:
            return False
        except Exception:
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        """
        if self.root is None:
            return []
        return self.root.findall(element_name)