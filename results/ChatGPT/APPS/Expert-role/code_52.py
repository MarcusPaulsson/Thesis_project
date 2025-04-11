def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(max_choose + 1)]
    dp[0][0] = 0  # Base case: choosing 0 elements gives sum 0 which is divisible by k

    for row in matrix:
        current_dp = [dp[i][:] for i in range(max_choose + 1)]
        row.sort(reverse=True)  # Sort row in descending order to maximize sum
        for count in range(1, max_choose + 1):
            for j in range(min(count, len(row)) + 1):
                if j > 0:
                    new_sum = sum(row[:j])
                    for mod in range(k):
                        if current_dp[count - j][mod] != -1:
                            new_mod = (mod + new_sum) % k
                            new_value = current_dp[count - j][mod] + new_sum
                            current_dp[count][new_mod] = max(current_dp[count][new_mod], new_value)
        dp = current_dp

    return max(dp[i][0] for i in range(max_choose + 1) if dp[i][0] != -1)

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))