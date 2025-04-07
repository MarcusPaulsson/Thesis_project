import urllib.parse

class UrlPath:
    """
    A utility for encapsulating and manipulating URL paths.
    """

    def __init__(self):
        """
        Initializes the UrlPath with an empty list of segments.
        """
        self.segments = []

    def add(self, segment):
        """
        Adds a segment to the path.

        Args:
            segment (str): The segment to add.  Should not contain '/'.
        """
        if not isinstance(segment, str):
            raise TypeError("Segment must be a string.")

        if '/' in segment:
            raise ValueError("Segment should not contain '/'.")

        self.segments.append(segment)

    def parse(self, path, charset='utf-8'):
        """
        Parses a URL path string into segments.

        Args:
            path (str): The URL path to parse.
            charset (str): The character encoding of the path. Defaults to 'utf-8'.
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")

        if not isinstance(charset, str):
            raise TypeError("Charset must be a string.")

        path = self._fix_path(path)
        if path:
            self.segments = path.split('/')
        else:
            self.segments = []


    @staticmethod
    def _fix_path(path):
        """
        Removes leading and trailing slashes from a path.

        Args:
            path (str): The path to fix.

        Returns:
            str: The fixed path.
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")

        return path.strip('/')

    def __str__(self):
        """
        Returns the path as a string.

        Returns:
            str: The concatenated path segments, separated by '/'.
        """
        return '/'.join(self.segments)

    def get_encoded_path(self, charset='utf-8'):
        """
        Returns the encoded path string.

        Args:
            charset (str): The character encoding to use. Defaults to 'utf-8'.

        Returns:
            str: The encoded path string.
        """
        encoded_segments = [urllib.parse.quote(segment, encoding=charset) for segment in self.segments]
        return '/'.join(encoded_segments)