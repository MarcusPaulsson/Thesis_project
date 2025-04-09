class IPAddress:
    """
    Class to process IP Addresses, including validation, retrieving octets, and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address: str):
        """
        Initialize the IP address with the specified address.
        
        :param ip_address: The IP address as a string.
        """
        self.ip_address = ip_address

    def is_valid(self) -> bool:
        """
        Check if the IP address is valid: four decimal digits (0-255) separated by '.'.
        
        :return: True if valid, False otherwise.
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
        Return a list of octets if the IP address is valid, otherwise return an empty list.
        
        :return: List of octets or an empty list if invalid.
        """
        return self.ip_address.split('.') if self.is_valid() else []

    def get_binary(self) -> str:
        """
        Return the binary representation of the IP address if valid, otherwise return an empty string.
        
        :return: Binary string representation or an empty string if invalid.
        """
        if self.is_valid():
            return '.'.join(f"{int(octet):08b}" for octet in self.ip_address.split('.'))
        return ''