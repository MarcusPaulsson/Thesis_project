class AvgPartition:
    """
    This is a class that partitions the given list into different blocks by specifying the number of partitions, with each block having a uniformly distributed length.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, and check if the number of partitions is greater than 0.
        """
        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        """
        if self.limit <= 0:
            raise ValueError("Limit must be greater than 0")
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return (size, remainder)


    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        """
        size, remainder = self.setNum()
        start = index * size + min(index, remainder)
        end = (index + 1) * size + min(index + 1, remainder)
        return self.lst[start:end]