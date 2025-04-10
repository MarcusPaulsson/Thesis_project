class AvgPartition:
    """
    This is a class that partitions the given list into different blocks by specifying the number of partitions, with each block having a uniformly distributed length.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions.
        Raises ValueError if the number of partitions is not positive.
        """
        if limit <= 0:
            raise ValueError("Number of partitions must be positive.")
        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: A tuple containing the base size of each block and the remainder.
        """
        base_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return (base_size, remainder)

    def get(self, index):
        """
        Retrieve a partition (block) from the list.
        :param index: The index of the partition to retrieve.
        :return: A list representing the partition.
        Raises IndexError if the index is out of bounds.
        """
        if not 0 <= index < self.limit:
            raise IndexError("Index out of bounds.")

        base_size, remainder = self.setNum()
        start = index * base_size + min(index, remainder)
        end = (index + 1) * base_size + min(index + 1, remainder)
        return self.lst[start:end]