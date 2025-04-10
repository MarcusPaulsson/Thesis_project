import socket
import re
import unittest


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


class IpUtilTest(unittest.TestCase):

    def test_is_valid_ipv4(self):
        self.assertTrue(IpUtil.is_valid_ipv4('192.168.0.123'))
        self.assertTrue(IpUtil.is_valid_ipv4('10.10.10.10'))
        self.assertTrue(IpUtil.is_valid_ipv4('0.0.0.0'))
        self.assertFalse(IpUtil.is_valid_ipv4('abc.168.0.123'))
        self.assertFalse(IpUtil.is_valid_ipv4('256.0.0.0'))

    def test_is_valid_ipv6(self):
        self.assertTrue(IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertFalse(IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334'))
        self.assertFalse(IpUtil.is_valid_ipv6('2001:0db8:85a3:2001:llll:8a2e:0370:7334'))
        self.assertFalse(IpUtil.is_valid_ipv6('2001:0db8:85a3:llll:llll:8a2e:0370:7334'))
        self.assertFalse(IpUtil.is_valid_ipv6('2001:0db8:85a3::llll:8a2e:0370:7334'))

    def test_get_hostname(self):
        self.assertIsNone(IpUtil.get_hostname('110.242.68.3'))
        self.assertIsNone(IpUtil.get_hostname('10.0.0.1'))
        self.assertEqual(IpUtil.get_hostname('0.0.0.0'), socket.gethostname())
        self.assertIsNone(IpUtil.get_hostname('0.0.0.1'))
        self.assertIsNone(IpUtil.get_hostname('0.0.0.2'))


if __name__ == '__main__':
    unittest.main()