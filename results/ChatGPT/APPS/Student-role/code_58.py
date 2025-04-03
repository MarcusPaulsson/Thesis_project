def min_cost_to_break_chocolate(t, queries):
    results = []
    
    for n, m, k in queries:
        if k == n * m:
            results.append(0)
            continue
        
        # DP table to store minimum cost for each (n, m, k)
        dp = [[[float('inf')] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case: 0 cost to get 0 squares
        for i in range(n + 1):
            for j in range(m + 1):
                dp[i][j][0] = 0
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                total_squares = i * j
                
                # If we can take the whole piece, cost is 0
                if total_squares <= k:
                    dp[i][j][total_squares] = 0
                
                # Try horizontal cuts
                for cut in range(1, i):
                    cost = j * j  # cost of cutting horizontally
                    for x in range(total_squares + 1):
                        if dp[cut][j][x] != float('inf'):
                            dp[i][j][x] = min(dp[i][j][x], dp[cut][j][x] + cost)
                        if dp[i - cut][j][x] != float('inf'):
                            dp[i][j][x] = min(dp[i][j][x], dp[i - cut][j][x] + cost)
                
                # Try vertical cuts
                for cut in range(1, j):
                    cost = i * i  # cost of cutting vertically
                    for x in range(total_squares + 1):
                        if dp[i][cut][x] != float('inf'):
                            dp[i][j][x] = min(dp[i][j][x], dp[i][cut][x] + cost)
                        if dp[i][j - cut][x] != float('inf'):
                            dp[i][j][x] = min(dp[i][j][x], dp[i][j - cut][x] + cost)
        
        results.append(dp[n][m][k])
    
    return results

# Example usage
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
results = min_cost_to_break_chocolate(t, queries)

for result in results:
    print(result)