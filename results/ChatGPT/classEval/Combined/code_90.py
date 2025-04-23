from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    A class to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize the URLHandler with a URL.
        
        :param url: The URL to be parsed.
        """
        self.url = url
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL.
        
        :return: The scheme of the URL as a string, or None if not present.
        """
        return self.parsed_url.scheme or None

    def get_host(self):
        """
        Get the host domain name of the URL.
        
        :return: The host domain name as a string, or None if not present.
        """
        return self.parsed_url.hostname or None

    def get_path(self):
        """
        Get the path of the resource in the URL.
        
        :return: The path as a string, or None if not present.
        """
        return self.parsed_url.path or None

    def get_query_params(self):
        """
        Get the query parameters from the URL.
        
        :return: A dictionary of query parameters, or None if there are no query parameters.
        """
        query_params = parse_qs(self.parsed_url.query)
        return {k: v[0] for k, v in query_params.items()} if query_params else None

    def get_fragment(self):
        """
        Get the fragment of the URL after the '#' character.
        
        :return: The fragment as a string, or None if not present.
        """
        return self.parsed_url.fragment or None