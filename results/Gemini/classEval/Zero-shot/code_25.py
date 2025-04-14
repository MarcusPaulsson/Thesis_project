import json

class CookiesUtil:
    """
    This is a class as utility for managing and manipulating Cookies, including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, reponse):
        """
        Gets the cookies from the specified response,and save it to cookies_file.
        :param reponse: The response to get cookies from, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        >>> cookies_util.cookies
        {'key1': 'value1', 'key2': 'value2'}

        """
        if 'cookies' in reponse:
            self.cookies = reponse['cookies']
        else:
            self.cookies = None

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.load_cookies()
        {'key1': 'value1', 'key2': 'value2'}

        """
        try:
            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
        except FileNotFoundError:
            self.cookies = {}
        except json.JSONDecodeError:
            self.cookies = {}
        if self.cookies and 'cookies' in self.cookies:
            return self.cookies['cookies']
        return self.cookies

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        >>> cookies_util = CookiesUtil('cookies.json')
        >>> cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        >>> cookies_util._save_cookies()
        True

        """
        if not self.cookies_file:
            return False
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f)
            return True
        except Exception:
            return False

    def set_cookies(self, request):
        """
        Sets the cookies to the specified request.
        :param request: The request to set cookies to, dict.
        :return: None
        """
        request['cookies'] = f"cookies={self.cookies}"