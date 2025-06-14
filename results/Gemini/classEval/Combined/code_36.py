from datetime import datetime

class EmailClient:
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space
    """

    def __init__(self, addr, capacity) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        if self.is_full_with_one_more_email(size):
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email = {
            'sender': self.addr,
            'receiver': recv.addr if isinstance(recv, EmailClient) else recv,
            'content': content,
            'size': size,
            'time': timestamp,
            'state': 'unread'
        }

        if isinstance(recv, EmailClient):
            recv.inbox.append(email)
            return True
        else:
            return False

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
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
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        total_size = 0
        for email in self.inbox:
            total_size += email['size']
        return total_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        if not self.inbox:
            return

        occupied_size = self.get_occupied_size()
        if occupied_size + size <= self.capacity:
            return

        emails_to_remove = []
        freed_space = 0
        for email in self.inbox:
            emails_to_remove.append(email)
            freed_space += email['size']
            if occupied_size - freed_space + size <= self.capacity:
                break

        for email in emails_to_remove:
            self.inbox.remove(email)