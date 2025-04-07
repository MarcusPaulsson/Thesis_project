import socket
import ipaddress


class IpUtil:
    """
    Utility class for IP address manipulation and validation.
    """

    @staticmethod
    def is_valid_ipv4(ip_address: str) -> bool:
        """
        Check if the given IP address is a valid IPv4 address.

        Args:
            ip_address: The IP address to check.

        Returns:
            True if the IP address is a valid IPv4 address, False otherwise.

        Examples:
            >>> IpUtil.is_valid_ipv4('192.168.0.123')
            True
            >>> IpUtil.is_valid_ipv4('256.0.0.0')
            False
        """
        try:
            ipaddress.IPv4Address(ip_address)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_ipv6(ip_address: str) -> bool:
        """
        Check if the given IP address is a valid IPv6 address.

        Args:
            ip_address: The IP address to check.

        Returns:
            True if the IP address is a valid IPv6 address, False otherwise.

        Examples:
            >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
            True
            >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
            False
        """
        try:
            ipaddress.IPv6Address(ip_address)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_hostname(ip_address: str) -> str | None:
        """
        Get the hostname associated with the given IP address.

        Args:
            ip_address: The IP address to get the hostname for.

        Returns:
            The hostname associated with the IP address, or None if not found.

        Examples:
            >>> # doctest: +SKIP
            >>> IpUtil.get_hostname('110.242.68.3')
            'www.baidu.com'
            >>> # doctest: +SKIP
            >>> IpUtil.get_hostname('10.0.0.1')
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except (socket.herror, socket.gaierror):
            return None
        except Exception:
            return None