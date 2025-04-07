import socket
import re


class IpUtil:
    """
    This is a utility class for handling IP addresses, including validation and hostname retrieval.
    """

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv4('192.168.0.123')
        True
        >>> IpUtil.is_valid_ipv4('256.0.0.0')
        False
        """
        pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return re.match(pattern, ip_address) is not None

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address: string, the IP address to check
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
        :param ip_address: string, the IP address to get the hostname for
        :return: string or None, the hostname associated with the IP address or None if not found
        >>> IpUtil.get_hostname('110.242.68.3')
        'www.baidu.com'  # Note: This may vary depending on current DNS records
        >>> IpUtil.get_hostname('10.0.0.1')
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return None


# Unit tests
import unittest

class IpUtilTestIsValidIpv4(unittest.TestCase):
    def test_is_valid_ipv4_1(self):
        result = IpUtil.is_valid_ipv4('192.168.0.123')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_2(self):
        result = IpUtil.is_valid_ipv4('10.10.10.10')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_3(self):
        result = IpUtil.is_valid_ipv4('0.0.0.0')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_4(self):
        result = IpUtil.is_valid_ipv4('abc.168.0.123')
        self.assertEqual(result, False)

    def test_is_valid_ipv4_5(self):
        result = IpUtil.is_valid_ipv4('256.0.0.0')
        self.assertEqual(result, False)


class IpUtilTestIsValidIpv6(unittest.TestCase):
    def test_is_valid_ipv6_1(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertEqual(result, True)

    def test_is_valid_ipv6_2(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_3(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:2001:llll:8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_4(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:llll:llll:8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_5(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3::llll:8a2e:0370:7334')
        self.assertEqual(result, False)


class IpUtilTestGetHostname(unittest.TestCase):
    def test_get_hostname_1(self):
        result = IpUtil.get_hostname('110.242.68.3')
        self.assertEqual(result, None)

    def test_get_hostname_2(self):
        result = IpUtil.get_hostname('10.0.0.1')
        self.assertEqual(result, None)

    def test_get_hostname_3(self):
        result = IpUtil.get_hostname('0.0.0.0')
        self.assertEqual(result, socket.gethostname())  # Localhost

    def test_get_hostname_4(self):
        result = IpUtil.get_hostname('0.0.0.1')
        self.assertEqual(result, None)

    def test_get_hostname_5(self):
        result = IpUtil.get_hostname('0.0.0.2')
        self.assertEqual(result, None)


class IpUtilTest(unittest.TestCase):
    def test_IpUtil(self):
        result = IpUtil.is_valid_ipv4('192.168.0.123')
        self.assertEqual(result, True)

        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertEqual(result, True)

        result = IpUtil.get_hostname('110.242.68.3')
        self.assertEqual(result, None)