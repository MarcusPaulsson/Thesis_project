class AvgPartition:
    """
    Partitions a list into approximately equal-sized blocks.
    """

    def __init__(self, lst, limit):
        """
        Initializes the partitioner.

        Args:
            lst: The list to partition.
            limit: The number of partitions to create.  Must be a positive integer.

        Raises:
            ValueError: If limit is not a positive integer.
        """
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Limit must be a positive integer.")

        self.lst = lst
        self.limit = limit
        self.size = len(lst)
        self.base_size = self.size // self.limit
        self.remainder = self.size % self.limit

    def setNum(self):
        """
        Calculates the base size and remainder.  This is now done during initialization
        for efficiency.  This method remains for backwards compatibility and testing.

        Returns:
            A tuple containing the base size and remainder.
        """
        return (self.base_size, self.remainder)

    def get(self, index):
        """
        Returns a partition of the list.

        Args:
            index: The index of the partition to retrieve (0-based).

        Returns:
            A list representing the partition.  Returns an empty list if the index is out of bounds.

        Raises:
            IndexError: If the index is out of range (negative or >= limit).
        """
        if not 0 <= index < self.limit:
            raise IndexError("Index out of range.")

        start = index * self.base_size + min(index, self.remainder)
        end = (index + 1) * self.base_size + min(index + 1, self.remainder)
        return self.lst[start:end]