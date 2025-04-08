from itertools import combinations

def max_sum_divisible_by_k(n, m, k, matrix):
    max_select = m // 2
    total_max_sum = 0

    for row in matrix:
        possible_sums = set()
        
        # Generate all possible sums from selecting up to max_select elements
        for r in range(max_select + 1):
            for combo in combinations(row, r):
                possible_sums.add(sum(combo))
        
        # Filter sums to find the maximum that is divisible by k
        divisible_sums = [s for s in possible_sums if s % k == 0]
        total_max_sum += max(divisible_sums, default=0)  # Use default=0 to handle empty case

    return total_max_sum

# Reading input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculating the maximum sum divisible by k
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)