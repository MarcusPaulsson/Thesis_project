from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    A class for handling URLs, allowing extraction of scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize the URLHandler with the provided URL.
        
        :param url: The URL to be parsed.
        """
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL.
        
        :return: str or None - the scheme of the URL.
        """
        return self.parsed_url.scheme or None

    def get_host(self):
        """
        Get the host domain name of the URL.
        
        :return: str or None - the host domain name of the URL.
        """
        return self.parsed_url.hostname or None

    def get_path(self):
        """
        Get the path of the resource in the URL.
        
        :return: str or None - the path of the resource of the URL.
        """
        return self.parsed_url.path or None

    def get_query_params(self):
        """
        Get the query parameters from the URL.
        
        :return: dict or None - the query parameters of the URL.
        """
        query_params = parse_qs(self.parsed_url.query)
        return {k: v[0] for k, v in query_params.items()} if query_params else None

    def get_fragment(self):
        """
        Get the fragment of the URL.
        
        :return: str or None - the fragment after '#' of the URL.
        """
        return self.parsed_url.fragment or None