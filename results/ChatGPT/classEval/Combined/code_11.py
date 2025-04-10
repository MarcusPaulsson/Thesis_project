class BitStatusUtil:
    """
    A utility class for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states: int, stat: int) -> int:
        """
        Add a status to the current status and validate parameters.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        """
        BitStatusUtil._validate_parameters(states, stat)
        return states | stat

    @staticmethod
    def has(states: int, stat: int) -> bool:
        """
        Check if the current status contains the specified status and validate parameters.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        """
        BitStatusUtil._validate_parameters(states, stat)
        return (states & stat) == stat

    @staticmethod
    def remove(states: int, stat: int) -> int:
        """
        Remove the specified status from the current status and validate parameters.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The status after removing the specified status, int.
        """
        BitStatusUtil._validate_parameters(states, stat)
        return states & ~stat

    @staticmethod
    def _validate_parameters(*args: int) -> None:
        """
        Validate that all parameters are non-negative and even.
        :param args: Parameters to be checked.
        :raises ValueError: If any parameter is negative or not even.
        """
        for arg in args:
            if arg < 0 or arg % 2 != 0:
                raise ValueError(f"{arg} is not even or negative")