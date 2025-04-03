def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations

    max_half_selection = m // 2
    total_max_sum = 0

    for row in matrix:
        row.sort(reverse=True)  # Sort the row in descending order to maximize sum
        current_max_sum = 0
        
        # Check all possible ways to choose up to max_half_selection elements
        for r in range(max_half_selection + 1):
            for combo in combinations(row, r):
                current_sum = sum(combo)
                if current_sum % k == 0:
                    current_max_sum = max(current_max_sum, current_sum)
        
        total_max_sum += current_max_sum

    return total_max_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)