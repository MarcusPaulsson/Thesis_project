def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_half = m // 2
    total_sum = 0

    for row in matrix:
        row.sort(reverse=True)
        best_sum = 0
        
        # Check all combinations of elements up to max_half
        for count in range(max_half + 1):
            for comb in combinations(row, count):
                current_sum = sum(comb)
                if current_sum % k == 0:
                    best_sum = max(best_sum, current_sum)
        
        total_sum += best_sum

    return total_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))