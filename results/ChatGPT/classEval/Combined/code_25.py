import json
import os

class CookiesUtil:
    """
    A utility class for managing and manipulating cookies, including methods for retrieving, saving, and setting cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = {}

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response and saves it to cookies_file.
        :param response: The response to get cookies from, dict.
        """
        self.cookies = response.get('cookies', {})
        self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        if os.path.exists(self.cookies_file):
            with open(self.cookies_file, 'r') as file:
                self.cookies = json.load(file)
        return self.cookies

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except (IOError, json.JSONDecodeError):
            return False

    def set_cookies(self, request):
        """
        Sets the cookies in the request.
        :param request: The request to set cookies in, dict.
        """
        request['cookies'] = self.cookies