class SignInSystem:
    """
    A system for managing user sign-in status.
    """

    def __init__(self):
        """
        Initializes the sign-in system with an empty user database.
        """
        self.users = {}  # Dictionary to store users and their sign-in status (username: bool)

    def add_user(self, username):
        """
        Adds a new user to the system.

        Args:
            username (str): The username of the user to add.

        Returns:
            bool: True if the user was added successfully, False if the user already exists.
        """
        if username in self.users:
            return False  # User already exists

        self.users[username] = False  # Add user with initial sign-in status as False (not signed in)
        return True  # User added successfully

    def sign_in(self, username):
        """
        Signs in an existing user.

        Args:
            username (str): The username of the user to sign in.

        Returns:
            bool: True if the user was signed in successfully, False if the user does not exist.
        """
        if username not in self.users:
            return False  # User does not exist

        self.users[username] = True  # Update sign-in status to True (signed in)
        return True  # User signed in successfully

    def check_sign_in(self, username):
        """
        Checks if a user is currently signed in.

        Args:
            username (str): The username of the user to check.

        Returns:
            bool: True if the user is signed in, False if the user does not exist or is not signed in.
        """
        if username not in self.users:
            return False  # User does not exist

        return self.users[username]  # Return the user's sign-in status

    def all_signed_in(self):
        """
        Checks if all users in the system are signed in.

        Returns:
            bool: True if all users are signed in, False otherwise.  Returns True if there are no users.
        """
        if not self.users:
            return True  # No users, so technically all are signed in (vacuously true)

        for signed_in in self.users.values():
            if not signed_in:
                return False  # At least one user is not signed in

        return True  # All users are signed in

    def all_not_signed_in(self):
        """
        Returns a list of usernames that are currently not signed in.

        Returns:
            list[str]: A list of usernames that are not signed in.
        """
        not_signed_in = [
            username for username, signed_in in self.users.items() if not signed_in
        ]  # List comprehension for efficiency
        return not_signed_in