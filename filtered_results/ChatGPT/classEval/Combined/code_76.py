class SignInSystem:
    """
    A sign-in system that manages user sign-in status, including adding users, signing in/out,
    checking sign-in status, and retrieving users who are signed in or not signed in.
    """

    def __init__(self):
        """Initializes the sign-in system with an empty user dictionary."""
        self.users = {}

    def add_user(self, username: str) -> bool:
        """
        Adds a user to the sign-in system.
        The initial sign-in state is set to False.
        
        :param username: The username to be added.
        :return: True if the user was added successfully, False if the user already exists.
        """
        if username in self.users:
            return False
        self.users[username] = False
        return True

    def sign_in(self, username: str) -> bool:
        """
        Signs in a user by changing their status to True.
        
        :param username: The username to be signed in.
        :return: True if the user is signed in successfully, False if the user does not exist.
        """
        if username not in self.users:
            return False
        self.users[username] = True
        return True

    def check_sign_in(self, username: str) -> bool:
        """
        Checks if a user is signed in.
        
        :param username: The username to check.
        :return: True if the user is signed in, False if the user does not exist or is not signed in.
        """
        return self.users.get(username, False)

    def all_signed_in(self) -> bool:
        """
        Checks if all registered users are signed in.
        
        :return: True if all users are signed in, False otherwise.
        """
        return all(self.users.values())

    def all_not_signed_in(self) -> list[str]:
        """
        Retrieves a list of usernames that are not signed in.
        
        :return: A list of usernames that are not signed in.
        """
        return [username for username, signed_in in self.users.items() if not signed_in]