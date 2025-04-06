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
        """
        try:
            octets = self.ip_address.split('.')
            if len(octets) != 4:
                return False
            for octet in octets:
                if not octet.isdigit():
                    return False
                num = int(octet)
                if num < 0 or num > 255:
                    return False
            return True
        except:
            return False

    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        """
        if self.is_valid():
            return self.ip_address.split('.')
        else:
            return []

    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        if not self.is_valid():
            return ''

        octets = self.get_octets()
        binary_octets = []
        for octet in octets:
            binary = bin(int(octet))[2:].zfill(8)
            binary_octets.append(binary)

        return '.'.join(binary_octets)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    ipaddress1 = IPAddress("10.10.10.10")
    print(f"IP Address: {ipaddress1.ip_address}")
    print(f"Is Valid: {ipaddress1.is_valid()}")
    print(f"Octets: {ipaddress1.get_octets()}")
    print(f"Binary: {ipaddress1.get_binary()}")

    ipaddress2 = IPAddress("256.256.256.256")
    print(f"\nIP Address: {ipaddress2.ip_address}")
    print(f"Is Valid: {ipaddress2.is_valid()}")
    print(f"Octets: {ipaddress2.get_octets()}")
    print(f"Binary: {ipaddress2.get_binary()}")

    ipaddress3 = IPAddress("192.168.1.a")
    print(f"\nIP Address: {ipaddress3.ip_address}")
    print(f"Is Valid: {ipaddress3.is_valid()}")
    print(f"Octets: {ipaddress3.get_octets()}")
    print(f"Binary: {ipaddress3.get_binary()}")