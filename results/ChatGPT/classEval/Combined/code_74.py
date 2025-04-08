class Server:
    """
    Server class that manages a whitelist, handles message sending and receiving, and displays information.
    """

    def __init__(self):
        """
        Initialize the server with an empty whitelist and structures for sending and receiving messages.
        """
        self.white_list = set()  # Use a set for O(1) average time complexity for lookups
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist if it does not already exist.
        :param addr: int, address to be added
        :return: updated whitelist or False if the address already exists
        """
        if addr in self.white_list:
            return False
        self.white_list.add(addr)
        return list(self.white_list)

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist if it exists.
        :param addr: int, address to be deleted
        :return: updated whitelist or False if the address does not exist
        """
        if addr not in self.white_list:
            return False
        self.white_list.remove(addr)
        return list(self.white_list)

    def recv(self, info):
        """
        Receive information if the address is on the whitelist.
        :param info: dict, information containing 'addr' and 'content'
        :return: content of the information if received, False if not on whitelist, or -1 for invalid input
        """
        if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
            return -1

        addr = info['addr']
        content = info['content']

        if addr not in self.white_list:
            return False

        self.receive_struct = info
        return content

    def send(self, info):
        """
        Send information containing address and content.
        :param info: dict, information containing 'addr' and 'content'
        :return: None if sent successfully, error message if input structure is incorrect
        """
        if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
            return "info structure is not correct"

        self.send_struct = info

    def show(self, struct_type):
        """
        Returns the structure of the specified type ('send' or 'receive').
        :param struct_type: string, type of struct to be returned
        :return: corresponding struct or False if type is invalid
        """
        if struct_type == 'send':
            return self.send_struct
        elif struct_type == 'receive':
            return self.receive_struct
        return False