from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.scheme
        except:
            return None

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.netloc
        except:
            return None

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.path
        except:
            return None

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        """
        try:
            parsed_url = urlparse(self.url)
            query_params = parse_qs(parsed_url.query)
            return {k: v[0] for k, v in query_params.items()}
        except:
            return None

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.fragment
        except:
            return None