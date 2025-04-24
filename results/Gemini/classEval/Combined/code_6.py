class AvgPartition:
    """
    Partitions a list into approximately equal-sized blocks.
    """

    def __init__(self, lst, limit):
        """
        Initializes the AvgPartition object.

        Args:
            lst: The list to partition.
            limit: The desired number of partitions.
        """
        if not isinstance(lst, list):
            raise TypeError("lst must be a list")
        if not isinstance(limit, int):
            raise TypeError("limit must be an integer")
        if limit <= 0:
            raise ValueError("limit must be greater than 0")

        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculates the base block size and the number of elements in the remainder.

        Returns:
            A tuple containing the base block size and the remainder.
        """
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Retrieves a specific partition (block) from the list.

        Args:
            index: The index of the desired partition (0-based).

        Returns:
            A list representing the requested partition.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0 or index >= self.limit:
            raise IndexError("Index out of bounds.")

        block_size, remainder = self.setNum()
        start = index * block_size + min(index, remainder)
        end = (index + 1) * block_size + min(index + 1, remainder)
        return self.lst[start:end]