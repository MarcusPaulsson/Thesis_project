import xml.etree.ElementTree as ET
import os


class XMLProcessor:
    """
    A class for handling XML files, including reading, writing, processing, and finding elements.
    """

    def __init__(self, file_name):
        """
        Initializes the XMLProcessor with the given file name.

        Args:
            file_name (str): The name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and sets the root element.

        Returns:
            ET.Element: The root element of the XML file, or None if an error occurs.
        """
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            print(f"Error: File not found: {self.file_name}")
            return None
        except ET.ParseError:
            print(f"Error: Failed to parse XML file: {self.file_name}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def write_xml(self, file_name):
        """
        Writes the current XML data to the specified file.

        Args:
            file_name (str): The name of the file to write the XML data to.

        Returns:
            bool: True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to write.  Please read an XML file first.")
            return False

        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing XML to {file_name}: {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in specific XML elements ('item' in this case) and writes the updated XML data to a new file.

        Args:
            file_name (str): The name of the file to write the modified XML data to.

        Returns:
            bool: True if the write operation is successful, False otherwise.
        """
        if self.root is None:
            print("Error: No XML data to process. Please read an XML file first.")
            return False

        try:
            for item in self.root.findall('item'):
                if item.text:  # Ensure the element has text before attempting to modify it
                    item.text = item.text.upper()

            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error processing and writing XML to {file_name}: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds all XML elements with the specified name.

        Args:
            element_name (str): The name of the elements to find.

        Returns:
            list: A list of found elements with the specified name.  Returns an empty list if root is None or no elements are found.
        """
        if self.root is None:
            print("Error: No XML data to search.  Please read an XML file first.")
            return []

        return self.root.findall(element_name)


if __name__ == '__main__':
    # Create a dummy XML file for testing
    xml_content = """
    <root>
        <item>apple</item>
        <item>banana</item>
        <item>orange</item>
    </root>
    """
    with open("test.xml", "w") as f:
        f.write(xml_content)

    # Example usage
    processor = XMLProcessor("test.xml")

    # Read XML
    root = processor.read_xml()
    if root is not None:
        print("XML read successfully.")

        # Find elements
        items = processor.find_element("item")
        print(f"Found {len(items)} 'item' elements:")
        for item in items:
            print(item.text)

        # Process XML data
        if processor.process_xml_data("processed.xml"):
            print("XML data processed and written to processed.xml")

        # Write XML
        if processor.write_xml("output.xml"):
            print("XML written to output.xml")

    # Clean up the dummy file
    os.remove("test.xml")
    if os.path.exists("output.xml"):
        os.remove("output.xml")
    if os.path.exists("processed.xml"):
        os.remove("processed.xml")