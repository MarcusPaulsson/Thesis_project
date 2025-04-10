class AvgPartition:
    """
    This class partitions the given list into blocks by specifying the number of partitions,
    with each block having a uniformly distributed length.
    """

    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and number of partitions.
        
        :param lst: List to be partitioned.
        :param limit: Number of partitions, must be greater than 0.
        :raises ValueError: If limit is less than or equal to 0.
        """
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0.")
        self.lst = lst
        self.limit = limit

    def _calculate_partition_sizes(self):
        """
        Calculate the size of each block and the remainder of the division.
        
        :return: Tuple containing the size of each block and the remainder.
        """
        total_length = len(self.lst)
        block_size = total_length // self.limit
        remainder = total_length % self.limit
        return block_size, remainder

    def get(self, index):
        """
        Retrieve the corresponding block based on the index of the partition.
        
        :param index: The index of the partition, must be within the valid range.
        :return: The corresponding block, list.
        :raises IndexError: If index is out of range.
        """
        if index < 0 or index >= self.limit:
            raise IndexError("Index out of range.")

        block_size, remainder = self._calculate_partition_sizes()
        start = index * block_size + min(index, remainder)
        end = start + block_size + (1 if index < remainder else 0)
        return self.lst[start:end]


# Unit tests
import unittest

class AvgPartitionTestSetNum(unittest.TestCase):
    def test_setNum(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a._calculate_partition_sizes(), (2, 0))

    def test_setNum_2(self):
        a = AvgPartition([1, 2, 3, 4, 5], 2)
        self.assertEqual(a._calculate_partition_sizes(), (2, 1))

    def test_setNum_3(self):
        a = AvgPartition([1, 2, 3, 4, 5], 3)
        self.assertEqual(a._calculate_partition_sizes(), (1, 2))

    def test_setNum_4(self):
        a = AvgPartition([1, 2, 3, 4, 5], 4)
        self.assertEqual(a._calculate_partition_sizes(), (1, 1))

    def test_setNum_5(self):
        a = AvgPartition([1, 2, 3, 4, 5], 5)
        self.assertEqual(a._calculate_partition_sizes(), (1, 0))

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

    def test_get_index_out_of_range(self):
        a = AvgPartition([1, 2, 3, 4], 2)
        with self.assertRaises(IndexError):
            a.get(2)

if __name__ == "__main__":
    unittest.main()