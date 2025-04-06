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
            return self.url.split("://")[0]
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
            url_parts = self.url.split("://")
            if len(url_parts) > 1:
                host_and_path = url_parts[1]
            else:
                host_and_path = url_parts[0]

            host = host_and_path.split("/")[0]

            return host
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
            url_parts = self.url.split("://")
            if len(url_parts) > 1:
                host_and_path = url_parts[1]
            else:
                return None

            path = "/" + "/".join(host_and_path.split("/")[1:])

            return path
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
            path = self.get_path()
            if path is None:
                return {}

            query_string = path.split("?")[1] if "?" in path else ""
            fragment = query_string.split("#")[0] if "#" in query_string else query_string

            params = {}
            for pair in fragment.split("&"):
                if "=" in pair:
                    key, value = pair.split("=")
                    params[key] = value
            return params
        except:
            return {}


    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
        try:
            if "#" in self.url:
                return self.url.split("#")[1]
            else:
                return None
        except:
            return None