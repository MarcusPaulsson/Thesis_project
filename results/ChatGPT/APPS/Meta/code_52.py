def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements_per_row = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is achievable with 0 elements

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)[:max_elements_per_row]
        current_dp = dp[i - 1][:]  # Copy previous row dp

        for j in range(1 << len(row)):
            current_sum = 0
            count = 0
            for bit in range(len(row)):
                if j & (1 << bit):
                    current_sum += row[bit]
                    count += 1
            if count <= max_elements_per_row:
                mod = current_sum % k
                if current_dp[mod] < current_sum:
                    current_dp[mod] = current_sum

        for mod in range(k):
            if dp[i - 1][mod] != -1:
                new_sum = dp[i - 1][mod]
                new_mod = (new_sum + current_dp[mod]) % k
                if dp[i][new_mod] < new_sum + current_dp[mod]:
                    dp[i][new_mod] = new_sum + current_dp[mod]

        dp[i] = current_dp

    return max(dp[n])

# Read input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)