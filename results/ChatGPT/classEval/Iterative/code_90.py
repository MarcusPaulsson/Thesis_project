from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    The class supports handling URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler with a URL.
        :param url: str, the URL to be parsed
        """
        self.url = url
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL.
        :return: str or None, the scheme of the URL or None if not present.
        """
        return self.parsed_url.scheme or None

    def get_host(self):
        """
        Get the host domain name of the URL.
        :return: str or None, the host domain name or None if not present.
        """
        return self.parsed_url.hostname or None

    def get_path(self):
        """
        Get the resource path of the URL, including query and fragment.
        :return: str or None, the resource path or None if not present.
        """
        path = self.parsed_url.path
        query = f'?{self.parsed_url.query}' if self.parsed_url.query else ''
        fragment = f'#{self.parsed_url.fragment}' if self.parsed_url.fragment else ''
        return path + query + fragment if path or query or fragment else None

    def get_query_params(self):
        """
        Get the query parameters of the URL as a dictionary.
        :return: dict or None, the query parameters or None if not present.
        """
        return {k: v[0] for k, v in parse_qs(self.parsed_url.query).items()} if self.parsed_url.query else None

    def get_fragment(self):
        """
        Get the fragment of the URL.
        :return: str or None, the fragment or None if not present.
        """
        return self.parsed_url.fragment or None