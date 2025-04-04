import socket
import re


class IpUtil:
    """
    A utility class for IP address operations,
    including validation of IPv4/IPv6 addresses and hostname retrieval.
    """

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :param ip_address: str, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False
        """
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if re.match(pattern, ip_address):
            parts = list(map(int, ip_address.split('.')))
            return all(0 <= part < 256 for part in parts)
        return False

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address: str, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        True
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        False
        """
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address: str, the IP address to get the hostname for
        :return: str, the hostname associated with the IP address
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'
        >>> IpUtil.get_hostname('10.0.0.1')
        'localhost'
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return 'Hostname not found'