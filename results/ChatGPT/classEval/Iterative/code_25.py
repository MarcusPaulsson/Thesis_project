import json
import os

class CookiesUtil:
    """
    A utility class for managing and manipulating cookies, including methods for retrieving, saving, and setting cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The path to the cookies file, str.
        """
        self.cookies_file = cookies_file
        self.cookies = self.load_cookies()

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response and saves them to the cookies file.
        :param response: The response to get cookies from, dict.
        """
        self.cookies = response.get('cookies', {})
        self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies file into the cookies data.
        :return: The cookies data, dict.
        """
        if not os.path.exists(self.cookies_file):
            return {}

        try:
            with open(self.cookies_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies file.
        :return: True if successful, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f, indent=4)
            return True
        except IOError:
            return False