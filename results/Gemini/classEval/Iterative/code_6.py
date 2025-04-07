class AvgPartition:
    """
    Partitions a list into approximately equal-sized blocks.
    """

    def __init__(self, lst, num_partitions):
        """
        Initializes the AvgPartition object.

        Args:
            lst: The list to partition.
            num_partitions: The desired number of partitions.  Must be a positive integer.

        Raises:
            TypeError: if lst is not a list or num_partitions is not an integer.
            ValueError: if num_partitions is not positive.
        """
        if not isinstance(lst, list):
            raise TypeError("lst must be a list")
        if not isinstance(num_partitions, int):
            raise TypeError("num_partitions must be an integer")
        if num_partitions <= 0:
            raise ValueError("num_partitions must be positive")

        self.lst = lst
        self.num_partitions = num_partitions

    def get_partition(self, index):
        """
        Returns a specific partition of the list.

        Args:
            index: The index of the partition to retrieve (0-based).

        Returns:
            A list representing the requested partition.  Returns an empty list if the index is out of bounds.

        Raises:
            TypeError: if index is not an integer.
            IndexError: if index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("index must be an integer")

        list_length = len(self.lst)
        if index < 0 or index >= self.num_partitions:
          return [] # Or raise IndexError: index out of range

        base_block_size = list_length // self.num_partitions
        remainder = list_length % self.num_partitions

        start = index * base_block_size + min(index, remainder)
        end = (index + 1) * base_block_size + min(index + 1, remainder)

        return self.lst[start:end]


if __name__ == '__main__':
    # Example Usage and Testing
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 1: Evenly divisible
    partitioner1 = AvgPartition(data, 2)
    print(f"Partition 1 (index 0): {partitioner1.get_partition(0)}")
    print(f"Partition 1 (index 1): {partitioner1.get_partition(1)}")

    # Test case 2: Remainder
    partitioner2 = AvgPartition(data, 3)
    print(f"Partition 2 (index 0): {partitioner2.get_partition(0)}")
    print(f"Partition 2 (index 1): {partitioner2.get_partition(1)}")
    print(f"Partition 2 (index 2): {partitioner2.get_partition(2)}")

    # Test case 3: More partitions than elements
    partitioner3 = AvgPartition(data, 15)
    for i in range(15):
        print(f"Partition 3 (index {i}): {partitioner3.get_partition(i)}")

    # Test case 4: Empty list
    partitioner4 = AvgPartition([], 5)
    for i in range(5):
        print(f"Partition 4 (index {i}): {partitioner4.get_partition(i)}")

    # Test case 5: Single element list
    partitioner5 = AvgPartition([5], 3)
    for i in range(3):
        print(f"Partition 5 (index {i}): {partitioner5.get_partition(i)}")

    #Example of Error Handling
    try:
        partitioner6 = AvgPartition([1,2],0)
    except ValueError as e:
        print(e)

    try:
        partitioner7 = AvgPartition([1,2], "a")
    except TypeError as e:
        print(e)