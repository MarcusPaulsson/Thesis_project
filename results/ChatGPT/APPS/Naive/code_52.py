def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations
    
    half_m = m // 2
    total_max_sum = 0
    
    for row in matrix:
        # Calculate all possible sums for choosing 0 to half_m elements
        possible_sums = set()
        for r in range(half_m + 1):
            for combo in combinations(row, r):
                possible_sums.add(sum(combo))
        
        # Filter sums that are divisible by k and find the maximum
        max_sum_in_row = max((s for s in possible_sums if s % k == 0), default=0)
        total_max_sum += max_sum_in_row
    
    return total_max_sum

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)