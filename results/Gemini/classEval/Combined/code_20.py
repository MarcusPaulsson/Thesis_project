from datetime import datetime

class Chat:
    """
    This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.
    """

    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: True if the user was added, False otherwise.
        """
        if username in self.users:
            return False
        else:
            self.users[username] = []
            return True

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: True if the user was removed, False otherwise.
        """
        if username in self.users:
            del self.users[username]
            return True
        else:
            return False

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: True if the message was sent, False otherwise.
        """
        if sender not in self.users or receiver not in self.users:
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_data = {'sender': sender, 'receiver': receiver, 'message': message, 'timestamp': timestamp}
        self.users[sender].append(message_data)
        self.users[receiver].append(message_data)
        return True

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        if username in self.users:
            return self.users[username]
        else:
            return []