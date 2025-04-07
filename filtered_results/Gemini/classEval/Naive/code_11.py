class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status.

        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        :raises TypeError: if states or stat is not an integer.
        :raises ValueError: if states or stat is negative.

        >>> BitStatusUtil.add(2, 4)
        6
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")

        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")

        return states | stat

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status.

        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        :raises TypeError: if states or stat is not an integer.
        :raises ValueError: if states or stat is negative.

        >>> BitStatusUtil.has(6, 2)
        True
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")

        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status.

        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The status after removing the specified status, int.
        :raises TypeError: if states or stat is not an integer.
        :raises ValueError: if states or stat is negative.

        >>> BitStatusUtil.remove(6, 2)
        4
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")

        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")
        return states & ~stat

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,
        if not, raise ValueError.

        :param args: Parameters to be checked, list.
        :raises TypeError: if args is not a list.
        :raises ValueError: if any element in args is not an integer or is negative or is odd.
        :return: None.

        >>> BitStatusUtil.check([2, 4, 6])
        >>> BitStatusUtil.check([2, 3, 4])
        Traceback (most recent call last):
        ...
        ValueError: 3 is not even
        """
        if not isinstance(args, list):
            raise TypeError("Args must be a list.")

        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"{arg} is not an integer")
            if arg < 0:
                raise ValueError(f"{arg} is negative")
            if arg % 2 != 0:
                raise ValueError(f"{arg} is not even")