from datetime import datetime
from typing import Dict, Optional, List

class EmailClient:
    """
    A simple email client for sending and receiving emails with size management.
    """

    def __init__(self, addr: str, capacity: float) -> None:
        """
        Initializes the EmailClient with an address and a capacity for the inbox.
        
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox: List[Dict] = []

    def send_to(self, recv: 'EmailClient', content: str, size: float) -> bool:
        """
        Sends an email to the specified receiver.
        
        :param recv: The receiver's email client, EmailClient.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's inbox is full.
        """
        if recv.is_full_with_one_more_email(size):
            return False

        email = {
            'sender': self.addr,
            'receiver': recv.addr,
            'content': content,
            'size': size,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'state': 'unread'
        }
        recv.inbox.append(email)
        return True

    def fetch(self) -> Optional[Dict]:
        """
        Retrieves the first unread email and marks it as read.
        
        :return: The first unread email, or None if no unread emails exist.
        """
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None

    def is_full_with_one_more_email(self, size: float) -> bool:
        """
        Checks if the inbox can accommodate one more email of the given size.
        
        :param size: The size of the email, float.
        :return: True if adding the email would exceed capacity, False otherwise.
        """
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self) -> float:
        """
        Calculates the total size of the emails in the inbox.
        
        :return: The total size of the emails, float.
        """
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size: float) -> None:
        """
        Clears the inbox by removing oldest emails until there is enough space for the given size.
        
        :param size: The size of the email to accommodate, float.
        """
        while self.get_occupied_size() + size > self.capacity and self.inbox:
            self.inbox.pop(0)