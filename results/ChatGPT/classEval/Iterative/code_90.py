from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    The class supports handling URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler with the given URL.
        :param url: str, the URL to be parsed
        """
        self.url = url
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL.
        :return: str, the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        'https'
        """
        return self.parsed_url.scheme

    def get_host(self):
        """
        Get the host domain name of the URL.
        :return: str, the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        'www.baidu.com'
        """
        return self.parsed_url.hostname

    def get_path(self):
        """
        Get the path of the URL, including query and fragment if present.
        :return: str, the path of the resource in the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        '/s'
        """
        return self.parsed_url.path

    def get_full_path(self):
        """
        Get the full path of the URL, including query and fragment.
        :return: str, the full path of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_full_path()
        '/s?wd=aaa&rsv_spt=1#page'
        """
        full_path = self.parsed_url.path
        if self.parsed_url.query:
            full_path += '?' + self.parsed_url.query
        if self.parsed_url.fragment:
            full_path += '#' + self.parsed_url.fragment
        return full_path

    def get_query_params(self):
        """
        Get the query parameters of the URL.
        :return: dict, the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {'wd': ['aaa'], 'rsv_spt': ['1']}
        """
        return parse_qs(self.parsed_url.query)

    def get_fragment(self):
        """
        Get the fragment of the URL.
        :return: str, the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        'page'
        """
        return self.parsed_url.fragment