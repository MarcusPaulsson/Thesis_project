from urllib.parse import urlparse, parse_qs


class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        if not isinstance(url, str):
            raise TypeError("URL must be a string")
        self.url = url

    def get_scheme(self):
        """
        Get the scheme of the URL.

        :return: string, If successful, return the scheme of the URL, otherwise None.
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.scheme or None
        except Exception:
            return None

    def get_host(self):
        """
        Get the host domain name of the URL.

        :return: string, If successful, return the host domain name of the URL, otherwise None.
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.netloc or None
        except Exception:
            return None

    def get_path(self):
        """
        Get the path of the URL.

        :return: string, If successful, return the path of the URL, otherwise None.
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        try:
            parsed_url = urlparse(self.url)
            path = parsed_url.path
            query = parsed_url.query
            fragment = parsed_url.fragment

            result = path
            if query:
                result += "?" + query
            if fragment:
                result += "#" + fragment

            return result or None  # Return None if the result is empty
        except Exception:
            return None

    def get_query_params(self):
        """
        Get the query parameters of the URL.

        :return: dict, If successful, return the request parameters of the URL, otherwise None.
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
        try:
            parsed_url = urlparse(self.url)
            query_params = parse_qs(parsed_url.query)
            if not query_params:
                return None
            return {k: v[0] for k, v in query_params.items()}
        except Exception:
            return None

    def get_fragment(self):
        """
        Get the fragment of the URL.

        :return: string, If successful, return the fragment of the URL, otherwise None.
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.fragment or None
        except Exception:
            return None