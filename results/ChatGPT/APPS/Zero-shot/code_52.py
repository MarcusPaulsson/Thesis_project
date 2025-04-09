def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: 0 elements chosen, sum is 0

    for i in range(1, n + 1):
        row = matrix[i - 1]
        row.sort(reverse=True)  # Sort to choose the largest elements
        current_dp = dp[i - 1][:]
        
        for count in range(1, max_choose + 1):
            if count > len(row):
                break
            current_sum = sum(row[:count])
            for j in range(k):
                if current_dp[j] != -1:
                    new_sum = current_dp[j] + current_sum
                    new_remainder = new_sum % k
                    if new_sum > dp[i][new_remainder]:
                        dp[i][new_remainder] = new_sum

        for j in range(k):
            dp[i][j] = max(dp[i][j], current_dp[j])

    return dp[n][0] if dp[n][0] != -1 else 0

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)