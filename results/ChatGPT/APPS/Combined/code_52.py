def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        current_dp = dp[i - 1][:]

        for j in range(1, max_elements + 1):
            if j > len(row):
                break
            
            current_sum = sum(row[:j])
            for r in range(k):
                if current_dp[r] != -1:
                    new_sum = current_dp[r] + current_sum
                    new_remainder = new_sum % k
                    dp[i][new_remainder] = max(dp[i][new_remainder], new_sum)

        for r in range(k):
            dp[i][r] = max(dp[i][r], current_dp[r])

    return max(dp[n])

# Example usage:
# n, m, k = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(max_sum_divisible_by_k(n, m, k, matrix))