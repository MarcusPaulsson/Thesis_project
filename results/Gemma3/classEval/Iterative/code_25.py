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
        """
        if 'cookies' in reponse:
            self.cookies = reponse['cookies']

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        try:
            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
            return self.cookies
        except FileNotFoundError:
            return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        if not self.cookies_file:
            return False
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f)
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False

    def set_cookies(self, request):
        """
        Sets the cookies in the request.
        :param request: The request to set cookies in, dict.
        """
        if self.cookies:
            request['cookies'] = f"cookies={json.dumps(self.cookies)}"