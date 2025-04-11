def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: 0 elements chosen, sum is 0

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)  # Sort row in descending order
        for j in range(max_elements + 1):
            current_sum = sum(row[:j])  # Sum of the top j elements
            for r in range(k):
                if dp[i - 1][r] != -1:  # If previous row has a valid sum
                    new_sum = dp[i - 1][r] + current_sum
                    new_remainder = new_sum % k
                    dp[i][new_remainder] = max(dp[i][new_remainder], new_sum)

        # Carry forward the previous row's values
        for r in range(k):
            dp[i][r] = max(dp[i][r], dp[i - 1][r])

    return max(dp[n])

# Example usage:
# n, m, k = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(max_sum_divisible_by_k(n, m, k, matrix))