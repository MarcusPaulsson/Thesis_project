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
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(self.url)
            if parsed_url.scheme:
                return parsed_url.scheme
            else:
                return None
        except:
            return None

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(self.url)
            if parsed_url.netloc:
                return parsed_url.netloc
            else:
                return None
        except:
            return None

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(self.url)
            if parsed_url.path:
                return parsed_url.path
            else:
                return None
        except:
            return None

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        try:
            from urllib.parse import urlparse, parse_qs
            parsed_url = urlparse(self.url)
            if parsed_url.query:
                return parse_qs(parsed_url.query)
            else:
                return None
        except:
            return None

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(self.url)
            if parsed_url.fragment:
                return parsed_url.fragment
            else:
                return None
        except:
            return None