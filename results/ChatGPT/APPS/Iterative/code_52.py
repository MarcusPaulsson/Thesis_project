def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [0] * k
    
    for row in matrix:
        # Sort the row in descending order to maximize the sum
        row.sort(reverse=True)
        
        # Temporary dp for the current row
        current_dp = dp[:]  # Copy previous state
        
        # For each number in the row, consider selecting up to max_choose elements
        for num in row[:max_choose]:
            for j in range(k):
                new_sum = current_dp[j] + num
                new_remainder = new_sum % k
                # Update the dp array to consider the new sum
                dp[new_remainder] = max(dp[new_remainder], new_sum)
    
    return dp[0]

# Read input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)