def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is divisible by k

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)[:max_elements]
        current_sums = {0}  # Start with the sum of choosing no elements

        for value in row:
            current_sums.update({s + value for s in current_sums})

        for mod in range(k):
            if dp[i - 1][mod] != -1:
                for s in current_sums:
                    new_sum = dp[i - 1][mod] + s
                    new_mod = new_sum % k
                    dp[i][new_mod] = max(dp[i][new_mod], new_sum)

    return max(dp[n])

# Example usage:
# n, m, k = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(max_sum_divisible_by_k(n, m, k, matrix))