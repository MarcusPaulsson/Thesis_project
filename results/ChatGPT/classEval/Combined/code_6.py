class AvgPartition:
    """
    This class partitions a given list into blocks by specifying the number of partitions,
    with each block having a uniformly distributed length.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions.
        :param lst: List to be partitioned.
        :param limit: Number of partitions, must be greater than 0.
        """
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0.")
        self.lst = lst
        self.limit = limit
        self.block_size, self.remainder = self._calculate_block_size()

    def _calculate_block_size(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: A tuple containing the size of each block and the remainder.
        """
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Retrieve the block corresponding to the given partition index.
        :param index: The index of the partition.
        :return: The corresponding block as a list.
        """
        if index < 0 or index >= self.limit:
            raise IndexError("Partition index out of range.")
        
        start = index * self.block_size + min(index, self.remainder)
        end = start + self.block_size + (1 if index < self.remainder else 0)
        return self.lst[start:end]

