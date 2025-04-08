class BitStatusUtil:
    """
    A utility class providing methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status, ensuring parameters are valid.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The updated status after adding the specified status, int.
        """
        BitStatusUtil.check([stat])  # Validate the status
        return states | stat  # Use bitwise OR to add the status

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status, ensuring parameters are valid.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        """
        BitStatusUtil.check([stat])  # Validate the status
        return (states & stat) == stat  # Use bitwise AND to check if the status is present

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status, ensuring parameters are valid.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The updated status after removing the specified status, int.
        """
        BitStatusUtil.check([stat])  # Validate the status
        return states & ~stat  # Use bitwise AND NOT to remove the status

    @staticmethod
    def check(args):
        """
        Validate that all provided arguments are non-negative and even.
        :param args: Parameters to be checked, list.
        :raises ValueError: If any argument is negative or odd.
        """
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} is negative")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")


# Test Cases
import unittest

class BitStatusUtilTestAdd(unittest.TestCase):
    def test_add(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 4), 6)

    def test_add_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 0), 2)

    def test_add_3(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(0, 0), 0)

    def test_add_4(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(0, 2), 2)

    def test_add_5(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 2), 2)


class BitStatusUtilTestHas(unittest.TestCase):
    def test_has(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(6, 2))

    def test_has_2(self):
        bit_status_util = BitStatusUtil()
        self.assertFalse(bit_status_util.has(8, 2))

    def test_has_3(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(6, 4))

    def test_has_4(self):
        bit_status_util = BitStatusUtil()
        self.assertFalse(bit_status_util.has(8, 6))

    def test_has_5(self):
        bit_status_util = BitStatusUtil()
        self.assertTrue(bit_status_util.has(6, 6))


class BitStatusUtilTestRemove(unittest.TestCase):
    def test_remove(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 2), 4)

    def test_remove_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(8, 2), 8)

    def test_remove_3(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 4), 2)

    def test_remove_4(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(8, 6), 8)

    def test_remove_5(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.remove(6, 6), 0)


class BitStatusUtilTestCheck(unittest.TestCase):
    def test_check(self):
        bit_status_util = BitStatusUtil()
        bit_status_util.check([2])

    def test_check_2(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([3])

    def test_check_3(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([-1])

    def test_check_4(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([2, 3, 4])

    def test_check_5(self):
        bit_status_util = BitStatusUtil()
        with self.assertRaises(ValueError):
            bit_status_util.check([2, 3, 4, 5])


class BitStatusUtilTestMain(unittest.TestCase):
    def test_main(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 4), 6)
        self.assertTrue(bit_status_util.has(6, 2))
        self.assertEqual(bit_status_util.remove(6, 2), 4)
        with self.assertRaises(ValueError):
            bit_status_util.check([2, 3, 4])

if __name__ == '__main__':
    unittest.main()