class SignInSystem:
    """
    A sign-in system that allows adding users, signing in/out,
    checking sign-in status, and retrieving lists of signed-in or not signed-in users.
    """

    def __init__(self):
        """Initialize the sign-in system with an empty user dictionary."""
        self.users = {}

    def add_user(self, username: str) -> bool:
        """
        Add a user to the sign-in system if the user does not already exist.
        The initial sign-in state for a new user is False.

        :param username: The username to be added.
        :return: True if the user is added successfully, False if the user already exists.
        """
        if username not in self.users:
            self.users[username] = False
            return True
        return False

    def sign_in(self, username: str) -> bool:
        """
        Sign in a user if the user exists in the system and change their state to signed in (True).

        :param username: The username to be signed in.
        :return: True if the user is signed in successfully, False if the user does not exist.
        """
        if username in self.users:
            self.users[username] = True
            return True
        return False

    def check_sign_in(self, username: str) -> bool:
        """
        Check if a user is signed in.

        :param username: The username to be checked.
        :return: True if the user is signed in, False if the user does not exist or is not signed in.
        """
        return self.users.get(username, False)

    def all_signed_in(self) -> bool:
        """
        Check if all users are signed in.

        :return: True if all users are signed in, False otherwise.
        """
        return all(self.users.values())

    def all_not_signed_in(self) -> list[str]:
        """
        Get a list of usernames that are not signed in.

        :return: A list of usernames that are not signed in.
        """
        return [username for username, signed_in in self.users.items() if not signed_in]