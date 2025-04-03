def max_sum_divisible_by_k(n, m, k, matrix):
    half_m = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)
        current_dp = dp[i - 1][:]
        
        for j in range(half_m + 1):
            if j > len(row):
                break
            sum_comb = sum(row[:j])
            for mod in range(k):
                if current_dp[mod] != -1:
                    new_mod = (mod + sum_comb) % k
                    new_sum = current_dp[mod] + sum_comb
                    if dp[i][new_mod] < new_sum:
                        dp[i][new_mod] = new_sum
        
        dp[i] = current_dp

    return dp[n][0]

# Input reading part
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calling the function and printing the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)