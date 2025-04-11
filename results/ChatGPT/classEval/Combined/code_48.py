import socket
import re



class IpUtil:
    """
    A utility class for IP address validation and hostname retrieval.
    """

    @staticmethod
    def is_valid_ipv4(ip_address: str) -> bool:
        """
        Validate if the given IP address is a valid IPv4 address.
        
        :param ip_address: The IP address to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.' \
                  r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.' \
                  r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.' \
                  r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
        return bool(re.match(pattern, ip_address))

    @staticmethod
    def is_valid_ipv6(ip_address: str) -> bool:
        """
        Validate if the given IP address is a valid IPv6 address.
        
        :param ip_address: The IP address to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,7}:|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|' \
                  r'^[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|' \
                  r'^:((?::[0-9a-fA-F]{1,4}){1,7}|:)|' \
                  r'^(?:[0-9a-fA-F]{1,4}:){1,7}:$'
        return bool(re.match(pattern, ip_address))

    @staticmethod
    def get_hostname(ip_address: str) -> str:
        """
        Retrieve the hostname associated with the given IP address.
        
        :param ip_address: The IP address to lookup.
        :return: The associated hostname or None if not found.
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return None
