import socket
import re


class IpUtil:
    """
    A utility class for IP address operations, including validation and hostname retrieval.
    """

    @staticmethod
    def is_valid_ipv4(ip_address: str) -> bool:
        """
        Check if the given IP address is a valid IPv4 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        """
        pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return bool(re.match(pattern, ip_address))

    @staticmethod
    def is_valid_ipv6(ip_address: str) -> bool:
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        """
        pattern = (
            r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,7}:|'
            r'(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|'
            r'[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|'
            r':(?::[0-9a-fA-F]{1,4}){1,7}|::|'
            r'(?:[0-9a-fA-F]{1,4}:){1,6}:$'
        )
        return bool(re.match(pattern, ip_address))

    @staticmethod
    def get_hostname(ip_address: str) -> str:
        """
        Get the hostname associated with the given IP address.
        :param ip_address: string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address or None if not resolvable
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return None