from itertools import combinations

def max_sum_divisible_by_k(matrix, n, m, k):
    max_sum = 0
    for row in matrix:
        for comb in combinations(row, min(m, m//2)):
            if sum(comb) % k == 0:
                max_sum = max(max_sum, sum(comb))
    return max_sum

n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(max_sum_divisible_by_k(matrix, n, m, k))