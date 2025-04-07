class Server:
    """
    This is a class that acts as a server, which handles a whitelist, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as empty dictionaries.
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists.
        :param addr: int, address to be added
        :return: new whitelist if added, False if the address already exists
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist.
        :param addr: int, address to be deleted
        :return: new whitelist if deleted, False if the address does not exist
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return self.white_list
        return False

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it.
        :param info: dict, information dictionary containing address and content
        :return: content of the information if successfully received, otherwise False
        """
        if isinstance(info, dict) and 'addr' in info and 'content' in info:
            if info['addr'] in self.white_list:
                self.receive_struct = info
                return info['content']
        return False

    def send(self, info):
        """
        Send information containing address and content.
        :param info: dict, information dictionary containing address and content
        :return: None if successfully sent, or a string indicating an error message if the structure is incorrect
        """
        if isinstance(info, dict) and 'addr' in info and 'content' in info:
            self.send_struct = info
        else:
            return "info structure is not correct"

    def show(self, type):
        """
        Returns struct of the specified type.
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: corresponding struct if type is valid, otherwise False
        """
        if type == 'send':
            return self.send_struct
        elif type == 'receive':
            return self.receive_struct
        return False