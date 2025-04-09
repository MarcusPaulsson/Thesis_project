def max_sum_divisible_by_k(n, m, k, matrix):
    max_select = m // 2
    dp = [[-1] * k for _ in range(max_select + 1)]
    dp[0][0] = 0

    for row in matrix:
        new_dp = [dp_row[:] for dp_row in dp]
        row.sort(reverse=True)

        for num in row[:max_select]:
            for count in range(max_select - 1, -1, -1):
                for mod in range(k):
                    if dp[count][mod] != -1:
                        new_sum = dp[count][mod] + num
                        new_mod = new_sum % k
                        new_dp[count + 1][new_mod] = max(new_dp[count + 1][new_mod], new_sum)
        dp = new_dp

    return max(dp[count][0] for count in range(max_select + 1) if dp[count][0] != -1)

# Reading input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Getting the result
result = max_sum_divisible_by_k(n, m, k, matrix)

# Printing the output
print(result)