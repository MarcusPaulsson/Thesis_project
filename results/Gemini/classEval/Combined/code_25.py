import json

class CookiesUtil:
    """
    Utility class for managing and manipulating cookies.

    Handles loading, saving, retrieving, and setting cookies.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.

        :param cookies_file: The path to the cookies file (JSON format).
        """
        self.cookies_file = cookies_file
        self.cookies = {}  # Initialize cookies as an empty dictionary

    def get_cookies(self, response):
        """
        Extracts cookies from a response dictionary.

        If the 'cookies' key exists in the response, its value is assigned to self.cookies.

        :param response: A dictionary representing the response, potentially containing a 'cookies' key.
        """
        if isinstance(response, dict) and 'cookies' in response:
            self.cookies = response['cookies']

    def load_cookies(self):
        """
        Loads cookies from the specified cookies file.

        If the file exists and contains valid JSON, the cookies are loaded into self.cookies.
        If the file does not exist or contains invalid JSON, self.cookies remains an empty dictionary.

        :return: A dictionary containing the loaded cookies. Returns an empty dictionary if loading fails.
        """
        if not self.cookies_file:
            return {}

        try:
            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
        except FileNotFoundError:
            self.cookies = {}
        except json.JSONDecodeError:
            self.cookies = {}
        return self.cookies

    def _save_cookies(self):
        """
        Saves the current cookies to the specified cookies file.

        :return: True if the cookies were successfully saved, False otherwise.
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
        Sets the cookies in the specified request dictionary.

        The cookies are added to the request dictionary under the 'cookies' key as a string representation
        of the cookie dictionary.

        :param request: The request dictionary to which cookies will be added.
        """
        if not isinstance(request, dict):
            return
        request['cookies'] = f"cookies={str(self.cookies)}"