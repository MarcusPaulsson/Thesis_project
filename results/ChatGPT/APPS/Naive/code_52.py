def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        current_dp = dp[i - 1][:]  # Copy previous row

        for j in range(1, max_elements + 1):
            if j <= len(row):
                sum_selected = sum(row[:j])
                for mod in range(k):
                    if current_dp[mod] != -1:
                        new_sum = current_dp[mod] + sum_selected
                        new_mod = new_sum % k
                        current_dp[new_mod] = max(current_dp[new_mod], new_sum)

        dp[i] = current_dp

    return max(dp[n])

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))