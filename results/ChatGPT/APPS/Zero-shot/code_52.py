def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(max_choose + 1)]
    dp[0][0] = 0

    for row in matrix:
        row.sort(reverse=True)
        current_dp = [dp[i][:] for i in range(max_choose + 1)]
        
        for i in range(1, max_choose + 1):
            for j in range(min(i, len(row))):
                if current_dp[i - 1][(j + 1) % k] != -1:
                    new_sum = current_dp[i - 1][(j + 1) % k] + row[j]
                    new_mod = new_sum % k
                    current_dp[i][new_mod] = max(current_dp[i][new_mod], new_sum)

        dp = current_dp

    return max(dp[i][0] for i in range(max_choose + 1))

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))