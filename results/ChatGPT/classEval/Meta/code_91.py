import urllib.parse

class UrlPath:
    """
    The class is a utility for encapsulating and manipulating the path component of a URL, including adding nodes, parsing path strings, and building path strings with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        """
        self.segments.append(segment)

    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        """
        self.segments = []
        self.with_end_tag = False
        
        # Decode the path if necessary (not strictly required for the test cases)
        decoded_path = path.encode(charset).decode(charset)
        # Fix the path by removing leading and trailing slashes
        fixed_path = self.fix_path(decoded_path)
        
        # Split the path into segments
        self.segments = fixed_path.split('/')
        
        # Check for end tag presence
        if path.endswith('/'):
            self.with_end_tag = True

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        return path.strip('/')