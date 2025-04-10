class Server:
    """
    This class represents a server that handles a whitelist, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initializes the server with an empty whitelist and structures for sent and received messages.
        """
        self.white_list = set()  # Using a set for O(1) average time complexity for lookups
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Adds an address to the whitelist if it does not already exist.
        :param addr: int, address to be added.
        :return: updated whitelist or False if the address already exists.
        """
        if addr in self.white_list:
            return False
        self.white_list.add(addr)
        return list(self.white_list)

    def del_white_list(self, addr):
        """
        Removes an address from the whitelist if it exists.
        :param addr: int, address to be deleted.
        :return: updated whitelist or False if the address does not exist.
        """
        if addr not in self.white_list:
            return False
        self.white_list.remove(addr)
        return list(self.white_list)

    def recv(self, info):
        """
        Receives information containing an address and content. Only accepts content from whitelisted addresses.
        :param info: dict, information dictionary containing 'addr' and 'content'.
        :return: content if received successfully, otherwise False or -1 for invalid input.
        """
        if not self._is_valid_info(info):
            return -1
        
        addr = info["addr"]
        if addr in self.white_list:
            self.receive_struct = info
            return info["content"]
        return False

    def send(self, info):
        """
        Sends information containing an address and content.
        :param info: dict, information dictionary containing 'addr' and 'content'.
        :return: None if sent successfully, otherwise an error message for invalid input.
        """
        if not self._is_valid_info(info):
            return "info structure is not correct"
        
        self.send_struct = info

    def show(self, struct_type):
        """
        Returns the structure of the specified type ('send' or 'receive').
        :param struct_type: string, the type of struct to be returned.
        :return: corresponding struct or False if the type is invalid.
        """
        if struct_type == 'send':
            return self.send_struct
        elif struct_type == 'receive':
            return self.receive_struct
        return False

    def _is_valid_info(self, info):
        """
        Validates the input information structure.
        :param info: dict, information to validate.
        :return: True if valid, otherwise False.
        """
        return isinstance(info, dict) and "addr" in info and "content" in info