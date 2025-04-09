def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements_to_choose = m // 2
    dp = [[-1] * k for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum of 0 is achievable with 0 elements

    for i in range(1, n + 1):
        row = sorted(matrix[i - 1], reverse=True)[:max_elements_to_choose]
        current_sums = [0]  # Start with the sum of 0 (choosing no elements)

        # Calculate all possible sums for the current row
        for j in range(1, len(row) + 1):
            current_sums.append(current_sums[-1] + row[j - 1])

        # Update dp for the current row
        for j in range(k):
            if dp[i - 1][j] != -1:  # Previous state is valid
                dp[i][j] = max(dp[i][j], dp[i - 1][j])  # Carry forward previous sums
                
                # Try to add combinations of elements from the current row
                for s in current_sums:
                    new_sum = dp[i - 1][j] + s
                    new_mod = new_sum % k
                    dp[i][new_mod] = max(dp[i][new_mod], new_sum)

    return max(dp[n])

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)