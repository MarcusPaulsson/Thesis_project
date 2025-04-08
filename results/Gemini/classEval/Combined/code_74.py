class Server:
    """
    A server class that manages a whitelist, sends and receives messages, and displays information.
    """

    def __init__(self):
        """
        Initializes the server with an empty whitelist and empty dictionaries for sent and received information.
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Adds an address to the whitelist if it's not already present.

        Args:
            addr: The address to add (must be hashable).

        Returns:
            True if the address was added, False otherwise.
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return True
        return False

    def del_white_list(self, addr):
        """
        Removes an address from the whitelist if it exists.

        Args:
            addr: The address to remove (must be hashable).

        Returns:
            True if the address was removed, False otherwise.
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
            return True
        return False

    def recv(self, info):
        """
        Receives information if the sender's address is on the whitelist.

        Args:
            info: A dictionary containing 'addr' (the sender's address) and 'content' (the message).

        Returns:
            The message content if the sender is on the whitelist and the info is valid.
            False if the sender is not on the whitelist.
            None if the info is invalid.
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return None

        addr = info["addr"]
        content = info["content"]

        if addr in self.white_list:
            self.receive_struct = info
            return content
        return False

    def send(self, info):
        """
        Sends information.  Stores the information in the `send_struct`.

        Args:
            info: A dictionary containing 'addr' (the recipient's address) and 'content' (the message).

        Returns:
            True if the information was successfully stored, False if the info is invalid.
        """
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return False

        self.send_struct = info
        return True

    def show(self, data_type):
        """
        Returns the stored send or receive data.

        Args:
            data_type:  A string, either "send" or "receive", indicating which data to return.

        Returns:
            The send_struct or receive_struct dictionary, or None if the data_type is invalid.
        """
        if data_type == "send":
            return self.send_struct
        if data_type == "receive":
            return self.receive_struct
        return None