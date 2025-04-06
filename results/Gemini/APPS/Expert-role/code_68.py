def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] = min(dp[i][j], k + 1)
    
    
    counts = [0] * (n + 1)
    for i in range(n + 1):
        counts[i] = dp[n][i]
        
    
    cost = 0
    
    
    for length in range(n, -1, -1):
        take = min(k, counts[length])
        cost += take * (n - length)
        k -= take
        
    if k > 0:
        print(-1)
    else:
        print(cost)

solve()