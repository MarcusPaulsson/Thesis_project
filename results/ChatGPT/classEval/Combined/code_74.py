class Server:
    """
    A class representing a server that manages a whitelist, handles message sending and receiving, and displays information.
    """

    def __init__(self):
        """
        Initialize the server with an empty whitelist and structures for sending and receiving messages.
        """
        self.white_list = set()  # Using a set for O(1) average time complexity for add/remove operations
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist if it does not already exist.
        
        :param addr: int, address to be added
        :return: updated whitelist or False if the address already exists
        """
        if addr not in self.white_list:
            self.white_list.add(addr)
            return list(self.white_list)
        return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist if it exists.
        
        :param addr: int, address to be deleted
        :return: updated whitelist or False if the address does not exist
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return list(self.white_list)
        return False

    def recv(self, info):
        """
        Receive information containing address and content. Only accept if the address is in the whitelist.
        
        :param info: dict, information dictionary containing address and content
        :return: content if successfully received, otherwise False
        """
        if isinstance(info, dict) and 'addr' in info and 'content' in info:
            addr = info['addr']
            if addr in self.white_list:
                self.receive_struct = info
                return info['content']
        return False

    def send(self, info):
        """
        Send information containing address and content.
        
        :param info: dict, information dictionary containing address and content
        :return: None if successfully sent, otherwise an error message
        """
        if isinstance(info, dict) and 'addr' in info and 'content' in info:
            self.send_struct = info
            return
        return "info structure is not correct"

    def show(self, type):
        """
        Returns the structure of the specified type.
        
        :param type: string, the type of struct to be returned, can be 'send' or 'receive'
        :return: corresponding struct or False if type is invalid
        """
        if type == 'send':
            return self.send_struct
        elif type == 'receive':
            return self.receive_struct
        return False