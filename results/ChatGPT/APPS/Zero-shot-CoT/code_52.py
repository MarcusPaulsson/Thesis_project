def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is divisible by k

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        current_dp = dp[i - 1][:]  # Copy previous row's dp

        for j in range(1, max_choose + 1):
            if j > len(row):
                break
            current_sum = sum(row[:j])
            for mod in range(k):
                if current_dp[mod] != -1:
                    new_sum = current_dp[mod] + current_sum
                    new_mod = new_sum % k
                    current_dp[new_mod] = max(current_dp[new_mod], new_sum)

        dp[i] = current_dp

    return max(dp[n])

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))