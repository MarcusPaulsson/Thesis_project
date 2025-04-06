class AvgPartition:
    """
    This class partitions a given list into uniformly distributed blocks based on the specified number of partitions.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and number of partitions.
        Raise ValueError if the number of partitions is less than or equal to 0.
        """
        if limit <= 0:
            raise ValueError("The number of partitions must be greater than 0.")
        
        self.lst = lst
        self.limit = limit

    def set_num(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: tuple containing the size of each block and the remainder.
        
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.set_num()
        (2, 0)
        """
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Retrieve the block corresponding to the given partition index.
        :param index: index of the partition, int.
        :return: the corresponding block, list.
        
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]
        >>> a.get(1)
        [3, 4]
        """
        if index < 0 or index >= self.limit:
            raise IndexError("Partition index out of range.")
        
        block_size, remainder = self.set_num()
        start = index * block_size + min(index, remainder)
        end = start + block_size + (1 if index < remainder else 0)
        return self.lst[start:end]