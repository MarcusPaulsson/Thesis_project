import urllib.parse

class UrlPath:
    """
    A utility class for encapsulating and manipulating the path component of a URL, 
    including adding segments, parsing path strings, and building path strings with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag 
        indicating the presence of an end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment: str):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        """
        self.segments.append(segment)

    def parse(self, path: str, charset: str):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        """
        decoded_path = urllib.parse.unquote(path, encoding=charset)
        stripped_path = self.fix_path(decoded_path)
        self.segments = stripped_path.split('/')
        self.with_end_tag = path.endswith('/')

    @staticmethod
    def fix_path(path: str) -> str:
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        return path.strip('/')

# Unit tests can be run with a testing framework like unittest.