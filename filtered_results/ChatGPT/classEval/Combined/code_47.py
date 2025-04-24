class IPAddress:
    """
    A class to process IP Addresses, including validation, retrieving octets, and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address: str):
        """
        Initialize the IP address to the specified address.
        :param ip_address: string
        """
        self.ip_address = ip_address

    def is_valid(self) -> bool:
        """
        Validate the IP address format. It should consist of four decimal digits (0-255) separated by '.'.
        :return: bool
        """
        octets = self.ip_address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                return False
        return True

    def get_octets(self) -> list:
        """
        Return a list of the four decimal numbers constituting the IP address if valid; otherwise, return an empty list.
        :return: list
        """
        return self.ip_address.split('.') if self.is_valid() else []

    def get_binary(self) -> str:
        """
        Return the binary representation of the IP address if valid; otherwise, return an empty string.
        :return: string
        """
        if self.is_valid():
            return '.'.join(format(int(octet), '08b') for octet in self.get_octets())
        return ''