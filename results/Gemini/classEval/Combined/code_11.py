class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Adds a status to the current status using bitwise OR.

        :param states: Current status (integer).
        :param stat: Status to be added (integer).
        :return: The status after adding the status (integer).
        :raises TypeError: if inputs are not integers.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        return states | stat

    @staticmethod
    def has(states, stat):
        """
        Checks if the current status contains the specified status using bitwise AND.

        :param states: Current status (integer).
        :param stat: Specified status (integer).
        :return: True if the current status contains the specified status, False otherwise (boolean).
        :raises TypeError: if inputs are not integers.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        """
        Removes the specified status from the current status using bitwise AND and NOT.

        :param states: Current status (integer).
        :param stat: Specified status to be removed (integer).
        :return: The status after removing the specified status (integer).
        :raises TypeError: if inputs are not integers.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        return states & (~stat)

    @staticmethod
    def check(args):
        """
        Checks if the provided arguments are valid based on the following criteria:
        1. Each argument must be an integer.
        2. Each argument must be greater than or equal to 0.
        3. Each argument must be an even number.

        :param args: A list of arguments to be checked.
        :raises TypeError: If any argument is not an integer.
        :raises ValueError: If any argument is less than 0 or not even.
        """
        if not isinstance(args, list):
            raise TypeError("Input must be a list.")

        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Arguments must be integers.")
            if arg < 0:
                raise ValueError(f"{arg} less than 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")