from datetime import datetime
from typing import List, Dict, Optional

class EmailClient:
    """
    A class representing an email client that can send and receive emails,
    check inbox capacity, and manage stored emails.
    """

    def __init__(self, addr: str, capacity: float) -> None:
        """
        Initializes the EmailClient with an email address and a storage capacity.
        
        :param addr: The email address.
        :param capacity: The maximum capacity of the inbox in bytes.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox: List[Dict] = []

    def send_to(self, recv: 'EmailClient', content: str, size: float) -> bool:
        """
        Sends an email to another EmailClient instance.
        
        :param recv: The recipient EmailClient.
        :param content: The content of the email.
        :param size: The size of the email in bytes.
        :return: True if the email is sent successfully, False if the recipient's inbox is full.
        """
        if recv.is_full_with_one_more_email(size):
            return False
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email = {
            'sender': self.addr,
            'receiver': recv.addr,
            'content': content,
            'size': size,
            'time': timestamp,
            'state': 'unread'
        }
        recv.inbox.append(email)
        return True

    def fetch(self) -> Optional[Dict]:
        """
        Retrieves the first unread email from the inbox and marks it as read.
        
        :return: The first unread email if available, otherwise None.
        """
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None

    def is_full_with_one_more_email(self, size: float) -> bool:
        """
        Checks if adding an email of a given size would exceed the inbox capacity.
        
        :param size: The size of the email to be added.
        :return: True if the inbox would be full, False otherwise.
        """
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self) -> float:
        """
        Calculates the total size of all emails in the inbox.
        
        :return: The total size of emails in bytes.
        """
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size: float) -> None:
        """
        Clears the inbox by removing the oldest emails until there is enough space for a new email.
        
        :param size: The size of the email to accommodate.
        """
        while self.is_full_with_one_more_email(size) and self.inbox:
            self.inbox.pop(0)  # Remove the oldest email