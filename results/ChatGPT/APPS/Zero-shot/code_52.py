def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        row = matrix[i - 1]
        row.sort(reverse=True)
        current_dp = dp[i - 1][:]  # Copy previous row

        for j in range(1, max_choose + 1):
            if j > len(row):
                break
            sum_selected = sum(row[:j])
            for r in range(k):
                if current_dp[r] != -1:
                    new_sum = current_dp[r] + sum_selected
                    new_remainder = new_sum % k
                    if new_sum > dp[i][new_remainder]:
                        dp[i][new_remainder] = new_sum

        for r in range(k):
            dp[i][r] = max(dp[i][r], current_dp[r])

    return max(dp[n])

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)