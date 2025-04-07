def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_choose = m // 2
    total_sum = 0

    for row in matrix:
        max_row_sum = 0
        # Generate all combinations of the row with sizes from 0 to max_choose
        for r in range(max_choose + 1):
            for comb in combinations(row, r):
                current_sum = sum(comb)
                if current_sum % k == 0:
                    max_row_sum = max(max_row_sum, current_sum)
        
        total_sum += max_row_sum

    return total_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)