from datetime import datetime

class EmailClient:
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space
    """

    def __init__(self, addr, capacity):
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        if not isinstance(addr, str):
            raise TypeError("Address must be a string.")
        if not isinstance(capacity, (int, float)):
            raise TypeError("Capacity must be a number.")
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.addr = addr
        self.capacity = float(capacity)  # Ensure capacity is a float
        self.inbox = []

    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The EmailClient object of the receiver.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        if not isinstance(recv, EmailClient):
            raise TypeError("Receiver must be an EmailClient object.")
        if not isinstance(content, str):
            raise TypeError("Content must be a string.")
        if not isinstance(size, (int, float)):
            raise TypeError("Size must be a number.")
        if size <= 0:
            raise ValueError("Size must be positive.")
            
        if recv.is_full_with_one_more_email(size):
            return False
        else:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            email = {'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': float(size), 'time': dt_string, 'state': 'unread'}
            recv.inbox.append(email)
            return True

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict. Returns None if no unread emails.
        """
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        if not isinstance(size, (int, float)):
            raise TypeError("Size must be a number.")
        if size <= 0:
            raise ValueError("Size must be positive.")
        
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        total_size = 0.0
        for email in self.inbox:
            total_size += float(email.get('size', 0))  # Ensure size is treated as a float
        return total_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        if not isinstance(size, (int, float)):
            raise TypeError("Size must be a number.")
        if size <= 0:
            raise ValueError("Size must be positive.")
            
        while self.is_full_with_one_more_email(size):
            if not self.inbox:
                break
            self.inbox.pop(0)