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

