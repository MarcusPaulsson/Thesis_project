import socket
import re
import unittest


class IpUtil:
    """
    A utility class for IP address operations, including validation and hostname retrieval.
    """

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        """
        pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return re.match(pattern, ip_address) is not None

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address: string, the IP address to check
        :return: bool, True if the IP address is valid, False otherwise
        """
        pattern = (
            r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,7}:|'
            r'(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|'
            r'(?:[0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|'
            r'[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,6}|'
            r':((:[0-9a-fA-F]{1,4}){1,7}|:)|'
            r'fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|'
            r'::(ffff(:0{1,4}){0,1}:)?'
            r'((25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}|'
            r'([0-9a-fA-F]{1,4}:)((25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}))$'
        )
        return re.match(pattern, ip_address) is not None

    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :param ip_address: string, the IP address to get the hostname for
        :return: string, the hostname associated with the IP address or None if not resolvable
        """
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except (socket.herror, socket.gaierror):
            return None


class IpUtilTestIsValidIPv4(unittest.TestCase):
    def test_is_valid_ipv4(self):
        valid_ips = ['192.168.0.123', '10.10.10.10', '0.0.0.0']
        invalid_ips = ['abc.168.0.123', '256.0.0.0']

        for ip in valid_ips:
            self.assertTrue(IpUtil.is_valid_ipv4(ip))
        
        for ip in invalid_ips:
            self.assertFalse(IpUtil.is_valid_ipv4(ip))


class IpUtilTestIsValidIPv6(unittest.TestCase):
    def test_is_valid_ipv6(self):
        valid_ips = ['2001:0db8:85a3:0000:0000:8a2e:0370:7334']
        invalid_ips = [
            '2001:0db8:85a3:::8a2e:0370:7334',
            '2001:0db8:85a3:2001:llll:8a2e:0370:7334',
            '2001:0db8:85a3:llll:llll:8a2e:0370:7334',
            '2001:0db8:85a3::llll:8a2e:0370:7334'
        ]

        for ip in valid_ips:
            self.assertTrue(IpUtil.is_valid_ipv6(ip))
        
        for ip in invalid_ips:
            self.assertFalse(IpUtil.is_valid_ipv6(ip))


class IpUtilTestGetHostname(unittest.TestCase):
    def test_get_hostname(self):
        test_cases = [
            ('110.242.68.3', None),
            ('10.0.0.1', None),
            ('0.0.0.0', socket.gethostname()),
            ('0.0.0.1', None),
            ('0.0.0.2', None)
        ]

        for ip, expected in test_cases:
            self.assertEqual(IpUtil.get_hostname(ip), expected)


class IpUtilTest(unittest.TestCase):
    def test_ip_util_methods(self):
        self.assertTrue(IpUtil.is_valid_ipv4('192.168.0.123'))
        self.assertTrue(IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertIsNone(IpUtil.get_hostname('110.242.68.3'))


if __name__ == '__main__':
    unittest.main()