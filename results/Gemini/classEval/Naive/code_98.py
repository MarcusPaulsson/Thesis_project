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
            print(f"Error: File '{self.file_name}' not found.")
            return None
        except ET.ParseError:
            print(f"Error: Failed to parse XML file '{self.file_name}'.")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to write. Please read an XML file first.")
            return False

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error: Failed to write XML to file '{file_name}'. {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to process. Please read an XML file first.")
            return False

        # Example modification: Add a new attribute to all elements
        for element in self.root.iter():
            element.set('processed', 'true')

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error: Failed to write processed XML to file '{file_name}'. {e}")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        """
        if self.root is None:
            print("Error: No XML data to search. Please read an XML file first.")
            return []

        return self.root.findall(element_name)


if __name__ == '__main__':
    # Create a dummy XML file for testing
    xml_data = """
    <root>
        <item>apple</item>
        <item>banana</item>
        <item>orange</item>
    </root>
    """
    with open('test.xml', 'w') as f:
        f.write(xml_data)

    xml_processor = XMLProcessor('test.xml')
    root_element = xml_processor.read_xml()
    print(f"Root Element: {root_element}")

    success = xml_processor.write_xml('output.xml')
    print(f"Write XML Successful: {success}")

    success = xml_processor.process_xml_data('processed.xml')
    print(f"Process XML Successful: {success}")

    items = xml_processor.find_element('item')
    print("Found Items:")
    for item in items:
        print(item.text)