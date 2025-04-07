from datetime import datetime

class Chat:
    """
    A chat class with the functions of adding/removing users, sending messages, and retrieving messages.
    """

    def __init__(self):
        """
        Initializes the Chat with an empty dictionary to store users and their messages.
        """
        self.users = {}

    def add_user(self, username):
        """
        Adds a new user to the Chat.

        Args:
            username (str): The user's name.

        Returns:
            bool: True if the user was added successfully, False if the user already exists.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")
        if not username:
            raise ValueError("Username cannot be empty.")

        if username in self.users:
            return False
        self.users[username] = []
        return True

    def remove_user(self, username):
        """
        Removes a user from the Chat.

        Args:
            username (str): The user's name.

        Returns:
            bool: True if the user was removed successfully, False if the user does not exist.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        if username in self.users:
            del self.users[username]
            return True
        return False

    def send_message(self, sender, receiver, message):
        """
        Sends a message from one user to another.

        Args:
            sender (str): The sender's username.
            receiver (str): The receiver's username.
            message (str): The message content.

        Returns:
            bool: True if the message was sent successfully, False if either the sender or receiver does not exist.
        """
        if not isinstance(sender, str) or not isinstance(receiver, str) or not isinstance(message, str):
            raise TypeError("Sender, receiver, and message must be strings.")
        if not sender or not receiver or not message:
            raise ValueError("Sender, receiver, and message cannot be empty.")

        if sender not in self.users or receiver not in self.users:
            return False

        timestamp = datetime.now().isoformat()  # Use ISO format for better compatibility
        message_data = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'timestamp': timestamp
        }
        self.users[receiver].append(message_data)
        return True

    def get_messages(self, username):
        """
        Retrieves all messages for a specific user.

        Args:
            username (str): The user's name.

        Returns:
            list: A list of message dictionaries, each containing 'sender', 'receiver', 'message', and 'timestamp'.
                  Returns an empty list if the user does not exist.
        """
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        if username in self.users:
            return self.users[username]
        else:
            return []