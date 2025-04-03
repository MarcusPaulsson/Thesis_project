def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_elements = m // 2
    total_max_sum = 0

    # Iterate through each row
    for row in matrix:
        row.sort(reverse=True)  # Sort row in descending order to maximize sum
        current_max_sum = [0] * k  # To store max sum for each modulo class
        
        # Try all combinations of selecting up to max_elements
        for r in range(max_elements + 1):
            for comb in combinations(row, r):
                current_sum = sum(comb)
                current_max_sum[current_sum % k] = max(current_max_sum[current_sum % k], current_sum)
        
        total_max_sum += max(current_max_sum)

    return total_max_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)