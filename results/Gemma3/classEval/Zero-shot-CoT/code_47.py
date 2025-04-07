class IPAddress:
    """
    This is a class to process IP Address, including validating, getting the octets and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address


    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
        try:
            octets = self.ip_address.split(".")
            if len(octets) != 4:
                return False
            for octet in octets:
                if not octet.isdigit():
                    return False
                octet_int = int(octet)
                if octet_int < 0 or octet_int > 255:
                    return False
            return True
        except:
            return False


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        if self.is_valid():
            return self.ip_address.split(".")
        else:
            return []


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        if self.is_valid():
            octets = self.get_octets()
            binary_octets = []
            for octet in octets:
                binary_octets.append(bin(int(octet))[2:].zfill(8))
            return ".".join(binary_octets)
        else:
            return ''