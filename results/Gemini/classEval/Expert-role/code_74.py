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
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server = Server()
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return self.white_list
        else:
            return False

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        >>> server = Server()
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
        if type(info) != dict or "addr" not in info or "content" not in info:
            return -1

        addr = info.get("addr")
        content = info.get("content")

        if addr in self.white_list:
            self.receive_struct = info
            return content
        else:
            return False

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server = Server()
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
        if type(info) != dict or "addr" not in info or "content" not in info:
            return "info structure is not correct"
        self.send_struct = info
        return

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        >>> server = Server()
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False