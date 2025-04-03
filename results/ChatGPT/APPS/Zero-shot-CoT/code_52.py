def max_sum_divisible_by_k(n, m, k, matrix):
    from itertools import combinations
    
    max_choose = m // 2
    total_max_sum = 0
    
    for row in matrix:
        best_mod_sums = [0] * k
        
        # Check all combinations of choosing elements in the row
        for r in range(max_choose + 1):
            for comb in combinations(row, r):
                current_sum = sum(comb)
                best_mod_sums[current_sum % k] = max(best_mod_sums[current_sum % k], current_sum)
        
        # Update the total max sum considering the best choices for each row
        total_max_sum += max(best_mod_sums)
    
    return total_max_sum

# Input handling
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)