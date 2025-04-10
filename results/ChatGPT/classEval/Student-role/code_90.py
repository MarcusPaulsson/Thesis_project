import re
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
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        """
        return self.parsed_url.scheme if self.parsed_url.scheme else None

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        """
        return self.parsed_url.hostname if self.parsed_url.hostname else None

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        return self.parsed_url.path + ('?' + self.parsed_url.query if self.parsed_url.query else '') + ('#' + self.parsed_url.fragment if self.parsed_url.fragment else '')

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        """
        return {k: v[0] for k, v in parse_qs(self.parsed_url.query).items()} if self.parsed_url.query else None

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        return self.parsed_url.fragment if self.parsed_url.fragment else None