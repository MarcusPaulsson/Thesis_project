import urllib.parse

class UrlPath:
    """
    A utility class for encapsulating and manipulating the path component of a URL,
    including adding segments, parsing path strings, and building path strings 
    with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments.
        """
        self.segments = []

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add. Must be a non-empty string.
        :raises ValueError: if segment is an empty string.
        """
        if not segment:
            raise ValueError("Segment cannot be an empty string.")
        self.segments.append(segment)

    def parse(self, path, charset='utf-8'):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string (default is 'utf-8').
        """
        fixed_path = self.fix_path(path)
        self.segments = [urllib.parse.unquote(segment, encoding=charset) 
                         for segment in fixed_path.split('/') if segment]

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        return path.strip('/')

    def build(self):
        """
        Constructs the complete path string from the segments, adding leading and 
        trailing slashes if necessary.
        :return: str, the constructed path string.
        """
        return '/' + '/'.join(self.segments) + ('/' if self.segments else '')

    def clear(self):
        """
        Clears all segments in the UrlPath.
        """
        self.segments.clear()

    def __repr__(self):
        """
        Returns a string representation of the UrlPath object.
        """
        return f"UrlPath(segments={self.segments})"