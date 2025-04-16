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
            scheme = self.url.split("://")[0]
            return scheme
        except IndexError:
            return None

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        """
        try:
            host = self.url.split("://")[1].split("/")[0]
            return host
        except IndexError:
            return None

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        try:
            path = self.url.split("://")[1]
            return path
        except IndexError:
            return None

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        """
        try:
            query_string = self.url.split("?")[1].split("#")[0]
            params = {}
            for pair in query_string.split("&"):
                if "=" in pair:
                    key, value = pair.split("=")
                    params[key] = value
            return params
        except IndexError:
            return None

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        try:
            fragment = self.url.split("#")[1]
            return fragment
        except IndexError:
            return None