def max_sum_divisible_by_k(n, m, k, matrix):
    half_m = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is achievable with 0 rows

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        for j in range(half_m + 1):
            current_sum = sum(row[:j])
            for r in range(k):
                if dp[i - 1][r] != -1:  # If the previous sum is achievable
                    new_sum = dp[i - 1][r] + current_sum
                    new_mod = new_sum % k
                    if dp[i][new_mod] == -1 or new_sum > dp[i][new_mod]:
                        dp[i][new_mod] = new_sum
                        
        # Copy previous row values to current row for no-selection case
        for r in range(k):
            if dp[i - 1][r] != -1:
                if dp[i][r] == -1 or dp[i - 1][r] > dp[i][r]:
                    dp[i][r] = dp[i - 1][r]
    
    # The result will be the maximum sum that is divisible by k
    return dp[n][0] if dp[n][0] != -1 else 0

# Input parsing
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)