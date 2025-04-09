import urllib.parse

class UrlPath:
    """
    A utility for encapsulating and manipulating the path component of a URL,
    including adding nodes, parsing path strings, and building path strings with optional encoding.
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
        if isinstance(segment, str):
            self.segments.append(segment)

    def parse(self, path, charset='utf-8'):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string (default is 'utf-8').
        """
        fixed_path = self.fix_path(path)
        self.segments = fixed_path.split('/') if fixed_path else []
        self.with_end_tag = path.endswith('/')

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        return path.strip('/')

