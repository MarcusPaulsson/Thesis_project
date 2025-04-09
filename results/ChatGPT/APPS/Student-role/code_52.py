def max_sum_divisible_by_k(n, m, k, matrix):
    max_elements = m // 2
    dp = [[0] * k for _ in range(max_elements + 1)]
    
    for row in matrix:
        row.sort(reverse=True)
        new_dp = [dp[:] for dp in dp]
        
        for count in range(max_elements + 1):
            for j in range(k):
                if dp[count][j] > 0 or count == 0:  # Account for the initial 0 sum
                    for x in range(1, min(max_elements - count, len(row)) + 1):
                        sum_selected = sum(row[:x])
                        new_remainder = (j + sum_selected) % k
                        new_dp[count + x][new_remainder] = max(new_dp[count + x][new_remainder], dp[count][j] + sum_selected)
        
        dp = new_dp
    
    return max(dp[count][0] for count in range(max_elements + 1))

# Input handling
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_sum_divisible_by_k(n, m, k, matrix)
print(result)