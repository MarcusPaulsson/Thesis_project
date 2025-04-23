class AvgPartition:
    """
    This class partitions a given list into blocks of approximately equal size based on the specified number of partitions.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions.
        
        :param lst: List to be partitioned.
        :param limit: Number of partitions (must be greater than 0).
        """
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0.")
        self.lst = lst
        self.limit = limit

    def _calculate_block_size(self):
        """
        Calculate the size of each block and the remainder of the division.
        
        :return: Tuple containing the size of each block and the remainder.
        """
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Retrieve the block corresponding to the specified partition index.
        
        :param index: The index of the partition (0-based).
        :return: The corresponding block as a list.
        """
        if index < 0 or index >= self.limit:
            raise IndexError("Partition index out of range.")
        
        block_size, remainder = self._calculate_block_size()
        start = index * block_size + min(index, remainder)
        end = start + block_size + (1 if index < remainder else 0)
        return self.lst[start:end]