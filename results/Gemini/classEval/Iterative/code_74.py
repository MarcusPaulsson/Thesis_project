class Server:
    """
    A server class that manages a whitelist, sends/receives messages, and displays information.
    """

    def __init__(self):
        """
        Initializes the server with an empty whitelist and empty dictionaries for sent and received data.
        """
        self.white_list = set()  # Use a set for efficient membership checking
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
            self.white_list.add(addr)
            return True
        return False

    def del_white_list(self, addr):
        """
        Removes an address from the whitelist if it exists.

        Args:
            addr: The address to remove.

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
            info: A dictionary containing 'addr' (sender's address) and 'content' (the message).

        Returns:
            The content of the message if the sender is whitelisted, False otherwise.
        """
        if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
            print("Error: Invalid info format. Expected a dictionary with 'addr' and 'content' keys.")  #Add error handling
            return False

        addr = info['addr']
        if addr in self.white_list:
            self.receive_struct = info.copy() # Store a copy to prevent modification of the original info
            return info['content']
        return False

    def send(self, info):
        """
        Sends information by storing it in the send_struct.

        Args:
            info: A dictionary containing 'addr' (recipient's address) and 'content' (the message).

        Returns:
            None.
        """
        if not isinstance(info, dict) or 'addr' not in info or 'content' not in info:
            print("Error: Invalid info format. Expected a dictionary with 'addr' and 'content' keys.")  #Add error handling
            return

        self.send_struct = info.copy() #Again store a copy
        return

    def show(self, type):
        """
        Returns the stored send or receive structure.

        Args:
            type: A string, either 'send' or 'receive', specifying which structure to return.

        Returns:
            The corresponding structure (send_struct or receive_struct) if the type is valid, False otherwise.
        """
        if type == "send":
            return self.send_struct.copy() # Return a copy to prevent external modification
        elif type == "receive":
            return self.receive_struct.copy() #Return a copy
        else:
            print("Error: Invalid type.  Must be 'send' or 'receive'.") #Add error handling
            return False