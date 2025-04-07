class SignInSystem:
    """
    A simple sign-in system.
    """

    def __init__(self):
        """
        Initializes the sign-in system with an empty dictionary of users.
        """
        self.users = {}  # key: username (str), value: sign-in status (bool)

    def add_user(self, username):
        """
        Adds a user to the system.

        Args:
            username (str): The username to add.

        Returns:
            bool: True if the user was added, False if the user already exists.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        if username in self.users:
            return False
        else:
            self.users[username] = False
            return True

    def sign_in(self, username):
        """
        Signs in a user.

        Args:
            username (str): The username to sign in.

        Returns:
            bool: True if the user was signed in, False if the user does not exist.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        if username in self.users:
            self.users[username] = True
            return True
        else:
            return False

    def sign_out(self, username):
        """
        Signs out a user.

        Args:
            username (str): The username to sign out.

        Returns:
            bool: True if the user was signed out, False if the user does not exist.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")
        if username in self.users:
            self.users[username] = False
            return True
        else:
            return False

    def check_sign_in(self, username):
        """
        Checks if a user is signed in.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the user is signed in, False if the user does not exist or is not signed in.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        if username in self.users:
            return self.users[username]
        else:
            return False

    def all_signed_in(self):
        """
        Checks if all users are signed in.

        Returns:
            bool: True if all users are signed in, False otherwise.  Returns True if there are no users.
        """
        if not self.users:
            return True  # Handle the case where there are no users

        return all(self.users.values())

    def all_not_signed_in(self):
        """
        Returns a list of usernames that are not signed in.

        Returns:
            list: A list of usernames (strings) that are not signed in.
        """
        return [username for username, signed_in in self.users.items() if not signed_in]


if __name__ == '__main__':
    # Example Usage
    system = SignInSystem()

    print("Adding users:")
    print(f"Adding 'Alice': {system.add_user('Alice')}")  # Output: True
    print(f"Adding 'Bob': {system.add_user('Bob')}")    # Output: True
    print(f"Adding 'Alice' again: {system.add_user('Alice')}")  # Output: False

    print("\nChecking sign-in status:")
    print(f"Is 'Alice' signed in? {system.check_sign_in('Alice')}")  # Output: False
    print(f"Is 'Bob' signed in? {system.check_sign_in('Bob')}")    # Output: False
    print(f"Is 'Charlie' signed in? {system.check_sign_in('Charlie')}")  # Output: False

    print("\nSigning in users:")
    print(f"Signing in 'Alice': {system.sign_in('Alice')}")  # Output: True
    print(f"Signing in 'Charlie': {system.sign_in('Charlie')}")  # Output: False

    print("\nChecking sign-in status again:")
    print(f"Is 'Alice' signed in? {system.check_sign_in('Alice')}")  # Output: True
    print(f"Is 'Bob' signed in? {system.check_sign_in('Bob')}")    # Output: False

    print("\nList of not signed in users:")
    print(f"Not signed in: {system.all_not_signed_in()}")  # Output: ['Bob']

    print("\nAre all users signed in?")
    print(f"All signed in? {system.all_signed_in()}")  # Output: False

    print("\nSigning in Bob")
    system.sign_in("Bob")
    print(f"All signed in? {system.all_signed_in()}")

    print("\nSigning out Alice")
    system.sign_out("Alice")
    print(f"Not signed in: {system.all_not_signed_in()}")

    print("\nNo users yet")
    system2 = SignInSystem()
    print(f"All signed in? {system2.all_signed_in()}")