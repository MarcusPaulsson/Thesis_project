class ArrangementCalculator:

    def __init__(self, datas):
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        if not m:
            return math.factorial(n)
        elif n == m:
            return math.factorial(n)
        else:
            return math.factorial(n) // math.factorial(n-m)

    @staticmethod
    def count_all(n):
        return 2**n

    def select(self, m=None):
        if not m:
            m = len(self.datas)
        return list(itertools.permutations(self.datas, m))

    def select_all(self):
        return list(itertools.chain(*[list(itertools.combinations(self.datas, i) for i in range(1, len(self.datas)+1)]))