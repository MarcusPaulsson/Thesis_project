class BitStatusUtil:
    """
    A utility class for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states: int, stat: int) -> int:
        """
        Adds a status to the current status.

        Args:
            states: The current status (int).
            stat: The status to be added (int).

        Returns:
            The status after adding the specified status (int).

        Raises:
            TypeError: If states or stat are not integers.
            ValueError: If states or stat are negative.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")
        return states | stat

    @staticmethod
    def has(states: int, stat: int) -> bool:
        """
        Checks if the current status contains the specified status.

        Args:
            states: The current status (int).
            stat: The specified status to check for (int).

        Returns:
            True if the current status contains the specified status, False otherwise (bool).

        Raises:
            TypeError: If states or stat are not integers.
            ValueError: If states or stat are negative.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")
        return (states & stat) == stat

    @staticmethod
    def remove(states: int, stat: int) -> int:
        """
        Removes the specified status from the current status.

        Args:
            states: The current status (int).
            stat: The specified status to remove (int).

        Returns:
            The status after removing the specified status (int).

        Raises:
            TypeError: If states or stat are not integers.
            ValueError: If states or stat are negative.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("States and stat must be integers.")
        if states < 0 or stat < 0:
            raise ValueError("States and stat must be non-negative.")
        return states & ~stat

    @staticmethod
    def check(args: list) -> None:
        """
        Checks if the given arguments are valid.  Arguments must be non-negative and even.

        Args:
            args: A list of integers to check.

        Raises:
            TypeError: If args is not a list.
            TypeError: If any element in args is not an integer.
            ValueError: If any argument is negative or odd.
        """
        if not isinstance(args, list):
            raise TypeError("Args must be a list.")

        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("All arguments in args must be integers.")
            if arg < 0:
                raise ValueError(f"{arg} is less than 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} is not even")