def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations
    
    max_sum = 0
    
    for row in matrix:
        # Limit the number of elements we can choose in each row
        limit = m // 2
        
        # Generate all combinations of elements we can select from the row
        for r in range(limit + 1):
            for combo in combinations(row, r):
                current_sum = sum(combo)
                if current_sum % k == 0:
                    max_sum = max(max_sum, current_sum)
    
    return max_sum

# Input reading
n, m, k = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# Get the result
result = max_sum_divisible_by_k(n, m, k, matrix)

# Output the result
print(result)