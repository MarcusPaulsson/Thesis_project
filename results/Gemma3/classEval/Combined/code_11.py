class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("Inputs must be non-negative.")
        if states % 2 != 0 or stat % 2 != 0:
            raise ValueError("Inputs must be even.")
        return states | stat

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("Inputs must be non-negative.")
        if states % 2 != 0 or stat % 2 != 0:
            raise ValueError("Inputs must be even.")
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Inputs must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("Inputs must be non-negative.")
        if states % 2 != 0 or stat % 2 != 0:
            raise ValueError("Inputs must be even.")
        return states & ~stat

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even.
        :param args: Parameters to be checked,list.
        :return: None.
        """
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Inputs must be integers.")
            if arg < 0:
                raise ValueError("Inputs must be non-negative.")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")