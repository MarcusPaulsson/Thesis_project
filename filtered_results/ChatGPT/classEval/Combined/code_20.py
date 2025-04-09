from datetime import datetime

class Chat:
    """
    A chat class that allows adding/removing users, sending messages, and retrieving messages.
    """

    def __init__(self):
        """Initialize the Chat with an empty dictionary for users."""
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        
        :param username: The user's name, str.
        :return: True if the user was added, False if the user already exists.
        """
        if username not in self.users:
            self.users[username] = []
            return True
        return False

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        
        :param username: The user's name, str.
        :return: True if the user was removed, False if the user was not found.
        """
        return self.users.pop(username, None) is not None

    def send_message(self, sender, receiver, message):
        """
        Send a message from one user to another.
        
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

    def get_messages(self, username):
        """
        Get all messages for a user.
        
        :param username: The user's name, str.
        :return: A list of messages sent to/from the user.
        """
        return self.users.get(username, [])