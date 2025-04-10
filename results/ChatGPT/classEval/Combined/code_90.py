from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    Class to handle URL parsing and extraction of components such as scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url: str):
        """
        Initialize the URLHandler with a URL.
        
        :param url: The URL string to be parsed.
        """
        self.parsed_url = urlparse(url)

    def get_scheme(self) -> str:
        """
        Get the scheme of the URL.

        :return: The scheme of the URL or None if not present.
        """
        return self.parsed_url.scheme or None

    def get_host(self) -> str:
        """
        Get the host domain name from the URL.

        :return: The host domain name of the URL or None if not present.
        """
        return self.parsed_url.hostname or None

    def get_path(self) -> str:
        """
        Get the path of the resource from the URL.

        :return: The path of the resource of the URL or None if not present.
        """
        return self.parsed_url.path or None

    def get_query_params(self) -> dict:
        """
        Get the query parameters from the URL.

        :return: A dictionary of query parameters or None if not present.
        """
        query = parse_qs(self.parsed_url.query)
        return {k: v[0] for k, v in query.items()} if query else None

    def get_fragment(self) -> str:
        """
        Get the fragment after '#' in the URL.

        :return: The fragment of the URL or None if not present.
        """
        return self.parsed_url.fragment or None