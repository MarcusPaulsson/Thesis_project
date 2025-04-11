def max_sum_divisible_by_k(n, m, k, matrix):
    max_choose = m // 2
    dp = [[-1] * k for _ in range(max_choose + 1)]
    dp[0][0] = 0  # Base case: sum of 0 with 0 elements chosen

    for row in matrix:
        new_dp = [dp_row[:] for dp_row in dp]  # Copy the current dp state
        row.sort(reverse=True)  # Sort row to maximize sum
        for count in range(max_choose + 1):
            for j in range(min(count, len(row)) + 1):
                if j > 0:
                    current_sum = sum(row[:j])
                    for mod in range(k):
                        if dp[count - j][mod] != -1:
                            new_sum = dp[count - j][mod] + current_sum
                            new_mod = new_sum % k
                            new_dp[count][new_mod] = max(new_dp[count][new_mod], new_sum)
        dp = new_dp

    return max(dp[count][0] for count in range(max_choose + 1) if dp[count][0] != -1)

# Input reading
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_sum_divisible_by_k(n, m, k, matrix))