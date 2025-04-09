class Server:
    """
    This is a class as a server, which handles a white list, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist if it doesn't already exist.
        :param addr: int, address to be added
        :return: True if added, False if already exists
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return True
        else:
            return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist if it exists.
        :param addr: int, address to be deleted
        :return: True if deleted, False if not found
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return True
        else:
            return False

    def recv(self, info):
        """
        Receive information.  If the address is on the whitelist, return the content; otherwise, return False.
        :param info: dict, information dictionary containing address and content
        :return: content if successfully received, False otherwise
        """
        if isinstance(info, dict) and "addr" in info and "content" in info and info["addr"] in self.white_list:
            self.receive_struct = info
            return info["content"]
        else:
            return False

    def send(self, info):
        """
        Send information.
        :param info: dict, information dictionary containing address and content
        :return: None if successful, error message string otherwise
        """
        if isinstance(info, dict) and "addr" in info and "content" in info:
            self.send_struct = info
            return None
        else:
            return "info structure is not correct"

    def show(self, type):
        """
        Returns the struct of the specified type.
        :param type: string, the type of struct to be returned ('send' or 'receive')
        :return: the struct if type is valid, False otherwise
        """
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False