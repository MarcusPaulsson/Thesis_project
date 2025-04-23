from datetime import datetime

class Chat:
    """
    A chat class that allows adding/removing users, sending messages, and retrieving messages.
    """

    def __init__(self):
        """Initialize the Chat with an empty user dictionary."""
        self.users = {}

    def add_user(self, username: str) -> bool:
        """
        Add a new user to the Chat.
        
        :param username: The user's name.
        :return: True if the user was added, False if the user already exists.
        """
        if username in self.users:
            return False
        self.users[username] = []
        return True

    def remove_user(self, username: str) -> bool:
        """
        Remove a user from the Chat.
        
        :param username: The user's name.
        :return: True if the user was removed, False if the user does not exist.
        """
        return self.users.pop(username, None) is not None

    def send_message(self, sender: str, receiver: str, message: str) -> bool:
        """
        Send a message from one user to another.
        
        :param sender: The sender's name.
        :param receiver: The receiver's name.
        :param message: The message content.
        :return: True if the message was sent, False if either user does not exist.
        """
        if sender not in self.users or receiver not in self.users:
            return False
        
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

    def get_messages(self, username: str):
        """
        Retrieve all messages for a user.
        
        :param username: The user's name.
        :return: A list of messages sent to/from the user.
        """
        return self.users.get(username, [])