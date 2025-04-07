import json
import os
from typing import Dict, Optional, Union

class CookiesUtil:
    """
    Utility class for managing and manipulating cookies, including methods for retrieving, saving, and loading cookie data.
    """

    def __init__(self, cookies_file: str):
        """
        Initializes the CookiesUtil with the specified cookies file.

        Args:
            cookies_file: The path to the cookies file (JSON format).
        """
        self.cookies_file = cookies_file
        self.cookies: Dict[str, str] = {}  # Initialize cookies as an empty dictionary

    def get_cookies(self, response: Dict[str, Union[str, Dict[str, str]]]) -> None:
        """
        Extracts cookies from the response and saves them to the cookies file.

        Args:
            response: The response dictionary, expected to contain a 'cookies' key.
        """
        if 'cookies' in response and isinstance(response['cookies'], dict):
            self.cookies = response['cookies']
            self.save_cookies()  # Changed to public method
        else:
            self.cookies = {}

    def load_cookies(self) -> Dict[str, str]:
        """
        Loads cookies from the cookies file.

        Returns:
            A dictionary containing the loaded cookies.  Returns an empty dictionary if the file does not exist or contains invalid JSON.
        """
        try:
            if not os.path.exists(self.cookies_file):
                return {}

            with open(self.cookies_file, 'r') as f:
                self.cookies = json.load(f)
                if not isinstance(self.cookies, dict):  # Check if loaded data is a dictionary
                    self.cookies = {}  # Reset if not a dictionary
        except (FileNotFoundError, json.JSONDecodeError):
            self.cookies = {}
        return self.cookies

    def save_cookies(self) -> bool:
        """
        Saves the current cookies to the cookies file.

        Returns:
            True if the cookies were saved successfully, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as f:
                json.dump(self.cookies, f, indent=4)  # Added indent for readability
            return True
        except Exception as e:
            print(f"Error saving cookies: {e}")
            return False

if __name__ == '__main__':
    # Example usage
    cookies_file = 'my_cookies.json'
    cookies_util = CookiesUtil(cookies_file)

    # Load cookies (if they exist)
    loaded_cookies = cookies_util.load_cookies()
    print(f"Loaded cookies: {loaded_cookies}")

    # Simulate a response with cookies
    response_data = {'status': 'success', 'cookies': {'session_id': '12345', 'user_id': 'abcde'}}
    cookies_util.get_cookies(response_data)
    print(f"Current cookies after get_cookies: {cookies_util.cookies}")

    # Save the cookies
    if cookies_util.save_cookies():
        print("Cookies saved successfully.")
    else:
        print("Failed to save cookies.")

    # Load cookies again to verify
    loaded_cookies_again = cookies_util.load_cookies()
    print(f"Loaded cookies after saving: {loaded_cookies_again}")

    # Clean up: Remove the cookies file
    try:
        os.remove(cookies_file)
        print(f"Removed {cookies_file}")
    except FileNotFoundError:
        pass