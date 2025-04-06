class SignInSystem:
    """
    A class representing a sign-in system, including functionalities for adding users, 
    signing in/out, checking sign-in status, and retrieving signed-in/not signed-in users.
    """

    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}

    def add_user(self, username: str) -> bool:
        """
        Add a user to the sign-in system if the user doesn't already exist.
        The initial sign-in state is set to False.
        
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        """
        if username in self.users:
            return False
        self.users[username] = False
        return True

    def sign_in(self, username: str) -> bool:
        """
        Sign in a user if they exist in the users list and are not already signed in.
        
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist or is already signed in.
        """
        if username in self.users and not self.users[username]:
            self.users[username] = True
            return True
        return False

    def check_sign_in(self, username: str) -> bool:
        """
        Check if a user is signed in.
        
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        """
        return self.users.get(username, False)

    def all_signed_in(self) -> bool:
        """
        Check if all users are signed in.
        
        :return: bool, True if all users are signed in, False otherwise.
        """
        return all(self.users.values())

    def all_not_signed_in(self) -> list[str]:
        """
        Get a list of usernames that are not signed in.
        
        :return: list[str], a list of usernames that are not signed in.
        """
        return [username for username, signed_in in self.users.items() if not signed_in]