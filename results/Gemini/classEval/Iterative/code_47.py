import ipaddress

class IPAddress:
    """
    This is a class to process IP Address, including validating, getting the octets and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address: string
        """
        self.ip_address = ip_address
        self._octets = None
        self._is_valid = None


    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        >>> ipaddress = IPAddress("256.256.256.256")
        >>> ipaddress.is_valid()
        False
        """
        if self._is_valid is None:
            try:
                ipaddress.ip_address(self.ip_address)
                self._is_valid = True
                self._octets = self.ip_address.split('.')
            except ValueError:
                self._is_valid = False
                self._octets = []
        return self._is_valid


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ['10', '10', '10', '10']
        >>> ipaddress = IPAddress("256.256.256.256")
        >>> ipaddress.get_octets()
        []
        """
        if self.is_valid():
            return self._octets
        else:
            return []


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        '00001010.00001010.00001010.00001010'
        >>> ipaddress = IPAddress("256.256.256.256")
        >>> ipaddress.get_binary()
        ''
        """
        if self.is_valid():
            binary_octets = []
            for octet in self._octets:
                binary_octet = bin(int(octet))[2:].zfill(8)
                binary_octets.append(binary_octet)
            return '.'.join(binary_octets)
        else:
            return ''

if __name__ == '__main__':
    import doctest
    doctest.testmod()