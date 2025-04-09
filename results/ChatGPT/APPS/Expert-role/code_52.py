def max_sum_divisible_by_k(n, m, k, matrix):
    max_select = m // 2
    dp = [[0] * k for _ in range(max_select + 1)]

    for row in matrix:
        current_dp = [dp[:] for dp in dp]
        row.sort(reverse=True)
        for num in row[:max_select]:
            for j in range(max_select, 0, -1):
                for r in range(k):
                    new_sum = current_dp[j - 1][r] + num
                    current_dp[j][new_sum % k] = max(current_dp[j][new_sum % k], new_sum)
        dp = current_dp

    return max(dp[j][0] for j in range(max_select + 1))

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)