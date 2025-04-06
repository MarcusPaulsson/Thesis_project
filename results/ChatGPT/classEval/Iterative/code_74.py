class Server:
    """
    This is a class that acts as a server, which handles a whitelist, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initialize the whitelist as an empty set for faster lookups, and initialize the sending and receiving information as empty dictionaries.
        """
        self.white_list = set()
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists.
        :param addr: int, address to be added
        :return: new whitelist or False if the address already exists
        """
        if addr not in self.white_list:
            self.white_list.add(addr)
            return list(self.white_list)
        return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist.
        :param addr: int, address to be deleted
        :return: new whitelist or False if the address does not exist
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return list(self.white_list)
        return False

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it.
        :param info: dict, information dictionary containing address and content
        :return: content if successfully received, otherwise False
        """
        addr = info.get("addr")
        if addr in self.white_list:
            self.receive_struct[addr] = info['content']
            return info['content']
        return False

    def send(self, info):
        """
        Send information containing address and content.
        :param info: dict, information dictionary containing address and content
        :return: None if successfully sent, otherwise an error message
        """
        addr = info.get("addr")
        if addr in self.white_list:
            self.send_struct = info
        else:
            return 'Error: Address not in whitelist'

    def show(self, struct_type):
        """
        Returns struct of the specified type.
        :param struct_type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: corresponding struct if valid, otherwise False
        """
        if struct_type == 'send':
            return self.send_struct
        elif struct_type == 'receive':
            return self.receive_struct
        return False