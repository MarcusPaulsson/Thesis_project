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
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root_element = xml_processor.read_xml()
        >>> print(root_element)
        <Element 'root' at 0x7f8e3b7eb180>
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
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.write_xml('output.xml')
        >>> print(success)
        True
        """
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.process_xml_data('processed.xml')
        >>> print(success)
        True
        """
        if self.root is None:
            print("Error: XML root is None.  Please read the XML file first.")
            return False

        # Example: Add an attribute to the root element
        self.root.set('processed', 'true')

        # Example: Modify text of elements named 'item'
        for item in self.root.findall('.//item'):  # Use .// to find all 'item' elements
            item.text = item.text.upper()

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_element('item')
        >>> for item in items:
        >>>     print(item.text)
        apple
        banana
        orange
        """
        if self.root is None:
            print("Error: XML root is None.  Please read the XML file first.")
            return []

        return self.root.findall(f'.//{element_name}')  # Use .// to find all elements with the given name


if __name__ == '__main__':
    # Create a sample XML file for testing
    xml_data = """
    <root>
        <items>
            <item>apple</item>
            <item>banana</item>
            <item>orange</item>
        </items>
    </root>
    """
    with open('test.xml', 'w') as f:
        f.write(xml_data)

    # Example usage
    xml_processor = XMLProcessor('test.xml')
    root_element = xml_processor.read_xml()
    print(f"Root element: {root_element}")

    success = xml_processor.write_xml('output.xml')
    print(f"Write successful: {success}")

    success = xml_processor.process_xml_data('processed.xml')
    print(f"Process and write successful: {success}")

    items = xml_processor.find_element('item')
    print("Items found:")
    for item in items:
        print(item.text)