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
        self._octets = self._parse_ip()

    def _parse_ip(self):
        """
        Parses the IP address string into a list of integers, validating each octet.
        Returns a list of integers if the IP is valid, otherwise returns None.
        """
        try:
            octets = self.ip_address.split('.')
            if len(octets) != 4:
                return None

            int_octets = []
            for octet in octets:
                num = int(octet)
                if 0 <= num <= 255:
                    int_octets.append(num)
                else:
                    return None
            return int_octets
        except ValueError:
            return None


    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
        return self._octets is not None


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        if self._octets:
            return [str(octet) for octet in self._octets]
        return []


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        if not self.is_valid():
            return ''

        binary_octets = [bin(octet)[2:].zfill(8) for octet in self._octets]
        return '.'.join(binary_octets)