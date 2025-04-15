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

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response.
        :param response: The response to get cookies from, dict.
        """
        if 'cookies' in response:
            self.cookies = response['cookies']

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file.
        :return: The cookies data, dict.
        """
        try:
            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
            return self.cookies
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file.
        :return: True if successful, False otherwise.
        """
        if not self.cookies:
            return False
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f)
            return True
        except Exception:
            return False