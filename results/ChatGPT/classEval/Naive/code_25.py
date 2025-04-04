import json
import os

class CookiesUtil:
    """
    This is a class as utility for managing and manipulating Cookies, 
    including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = self.load_cookies()  # Load cookies at initialization

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
                return json.load(file)
        return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, 
        and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False