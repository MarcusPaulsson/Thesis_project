def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_elements_to_choose = m // 2
    total_sum = 0

    for row in matrix:
        # Generate all combinations of choosing elements from the row
        best_sum = 0
        for r in range(max_elements_to_choose + 1):
            for comb in combinations(row, r):
                current_sum = sum(comb)
                if current_sum % k == 0:
                    best_sum = max(best_sum, current_sum)
        total_sum += best_sum

    return total_sum

# Read input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result
result = max_sum_divisible_by_k(n, m, k, matrix)

# Print the result
print(result)