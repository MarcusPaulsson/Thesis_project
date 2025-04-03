class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        if limit <= 0:
            raise ValueError("Number of partitions should be greater than zero")
        self.limit = limit

    def setNum(self):
        size = len(self.lst) // self.limit
        rem = len(self.lst) % self.limit
        return (size + 1, rem)

    def get(self, index):
        size, rem = self.setNum()
        start_idx = index * size
        end_idx = start_idx + size - 1 + min(index, rem)
        return self.lst[start_idx:end_idx+1]