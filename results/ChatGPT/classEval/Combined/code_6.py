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


# Unit tests
import unittest

class AvgPartitionTestSetNum(unittest.TestCase):
    def test_setNum(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a._calculate_block_size(), (2, 0))

    def test_setNum_2(self):
        a = AvgPartition([1, 2, 3, 4, 5], 2)
        self.assertEqual(a._calculate_block_size(), (2, 1))

    def test_setNum_3(self):
        a = AvgPartition([1, 2, 3, 4, 5], 3)
        self.assertEqual(a._calculate_block_size(), (1, 2))

    def test_setNum_4(self):
        a = AvgPartition([1, 2, 3, 4, 5], 4)
        self.assertEqual(a._calculate_block_size(), (1, 1))

    def test_setNum_5(self):
        a = AvgPartition([1, 2, 3, 4, 5], 5)
        self.assertEqual(a._calculate_block_size(), (1, 0))

class AvgPartitionTestGet(unittest.TestCase):
    def test_get(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a.get(0), [1, 2])

    def test_get_2(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a.get(1), [3, 4])

    def test_get_3(self):
        a = AvgPartition([1, 2, 3, 4, 5], 2)
        self.assertEqual(a.get(0), [1, 2, 3])

    def test_get_4(self):
        a = AvgPartition([1, 2, 3, 4, 5], 2)
        self.assertEqual(a.get(1), [4, 5])

    def test_get_5(self):
        a = AvgPartition([1, 2, 3, 4, 5], 3)
        self.assertEqual(a.get(0), [1, 2])

class AvgPartitionTestMain(unittest.TestCase):
    def test_main(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a._calculate_block_size(), (2, 0))
        self.assertEqual(a.get(0), [1, 2])

if __name__ == '__main__':
    unittest.main()