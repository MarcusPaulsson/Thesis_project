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
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: True if the address was added, False otherwise.
        """
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return True

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: True if the address was deleted, False otherwise.
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return True
        else:
            return False

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: The content of the information if successfully received, False if the address is not on the whitelist, -1 if the info is invalid.
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return -1

        addr = info["addr"]
        content = info["content"]

        if addr in self.white_list:
            self.receive_struct = info
            return content
        else:
            return False

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: None if successfully sent, an error message string otherwise.
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return "info structure is not correct"

        self.send_struct = info
        return

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: The corresponding struct if type is 'send' or 'receive', False otherwise.
        """
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False