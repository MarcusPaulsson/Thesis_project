def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        for j in range(max_elements + 1):
            current_sum = sum(row[:j])
            for r in range(k):
                if dp[i - 1][r] != -1:
                    new_sum = dp[i - 1][r] + current_sum
                    new_mod = new_sum % k
                    dp[i][new_mod] = max(dp[i][new_mod], new_sum)

        # Also consider not taking any elements from this row
        for r in range(k):
            if dp[i - 1][r] != -1:
                dp[i][r] = max(dp[i][r], dp[i - 1][r])

    return max(dp[n])

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))