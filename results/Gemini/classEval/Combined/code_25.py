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
        self.cookies = {}

    def get_cookies(self, reponse):
        """
        Gets the cookies from the specified response.
        :param reponse: The response to get cookies from, dict.
        """
        if 'cookies' in reponse:
            self.cookies = reponse['cookies']

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file.
        :return: The cookies data, dict.
        """
        try:
            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
        except FileNotFoundError:
            self.cookies = {}
        except json.JSONDecodeError:
            self.cookies = {}

        if isinstance(self.cookies, dict):
            return self.cookies
        else:
            return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file.
        :return: True if successful, False otherwise.
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
        """
        request['cookies'] = "cookies=" + str(self.cookies)