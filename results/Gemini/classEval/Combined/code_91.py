import urllib.parse

class UrlPath:
    """
    A utility for encapsulating and manipulating URL path components.
    """

    def __init__(self):
        """
        Initializes the UrlPath with an empty list of segments and no end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the end of the path.

        Args:
            segment (str): The segment to add.
        """
        if not isinstance(segment, str):
            raise TypeError("Segment must be a string.")
        self.segments.append(segment)

    def parse(self, path, charset):
        """
        Parses a path string into segments.

        Args:
            path (str): The path to parse.
            charset (str):  encoding of the path string (no longer used).
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")

        path = self.fix_path(path)

        if path.endswith('/'):
            self.with_end_tag = True
            path = path[:-1]
        else:
            self.with_end_tag = False

        self.segments = path.split('/') if path else []


    @staticmethod
    def fix_path(path):
        """
        Removes leading and trailing slashes from a path.

        Args:
            path (str): The path to fix.

        Returns:
            str: The fixed path.
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")

        path = path.strip('/')
        return path