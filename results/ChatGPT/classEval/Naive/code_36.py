from datetime import datetime

class EmailClient:
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space.
    """

    def __init__(self, addr: str, capacity: float) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    def send_to(self, recv, content: str, size: float) -> bool:
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, EmailClient.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        if recv.is_full_with_one_more_email(size):
            return False
        
        email = {
            'sender': self.addr,
            'receiver': recv.addr,
            'content': content,
            'size': size,
            'time': datetime.now(),
            'state': 'unread'
        }
        recv.inbox.append(email)
        return True

    def fetch(self) -> dict:
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None

    def is_full_with_one_more_email(self, size: float) -> bool:
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self) -> float:
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size: float) -> None:
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        while self.get_occupied_size() + size > self.capacity and self.inbox:
            self.inbox.pop(0)  # Remove the oldest email