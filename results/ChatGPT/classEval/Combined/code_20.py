from datetime import datetime

class Chat:
    """
    A class representing a chat system with functionalities for user management and messaging.
    """

    def __init__(self):
        """
        Initialize the Chat with an empty dictionary for users.
        """
        self.users = {}

    def add_user(self, username: str) -> bool:
        """
        Add a new user to the Chat.

        :param username: The user's name, str.
        :return: True if the user was added, False if the user already exists.
        """
        if username not in self.users:
            self.users[username] = []
            return True
        return False

    def remove_user(self, username: str) -> bool:
        """
        Remove a user from the Chat.

        :param username: The user's name, str.
        :return: True if the user was removed, False if the user does not exist.
        """
        return self.users.pop(username, None) is not None

    def send_message(self, sender: str, receiver: str, message: str) -> bool:
        """
        Send a message from a user to another user.

        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message content, str.
        :return: True if the message was sent, False if sender or receiver does not exist.
        """
        if sender in self.users and receiver in self.users:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_data = {
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': timestamp
            }
            self.users[sender].append(message_data)
            self.users[receiver].append(message_data)
            return True
        return False

    def get_messages(self, username: str) -> list:
        """
        Retrieve all messages for a user.

        :param username: The user's name, str.
        :return: A list of messages associated with the user.
        """
        return self.users.get(username, [])