def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is divisible by k

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)[:max_elements]
        current_sums = {0}  # Start with the sum of choosing no elements

        for num in row:
            new_sums = {s + num for s in current_sums}  # Use set comprehension for new sums
            current_sums.update(new_sums)  # Merge new sums into current sums

        for s in current_sums:
            mod = s % k
            if dp[i - 1][mod] != -1:
                dp[i][mod] = max(dp[i][mod], dp[i - 1][mod] + s)

        for mod in range(k):
            if dp[i - 1][mod] != -1:
                dp[i][mod] = max(dp[i][mod], dp[i - 1][mod])

    return max(dp[n])

# Read input
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)