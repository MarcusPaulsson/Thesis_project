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
            dp[i][j] = min(dp[i][j], k)
    
    total_subsequences = 0
    for i in range(n + 1):
        total_subsequences += dp[n][i]
    
    total_subsequences = min(total_subsequences, k)
    
    if total_subsequences < k:
        print(-1)
        return
    
    cost = 0
    current_len = n
    
    while k > 0:
        if dp[n][current_len] >= k:
            cost += (n - current_len) * k
            k = 0
        else:
            cost += (n - current_len) * dp[n][current_len]
            k -= dp[n][current_len]
        current_len -= 1
        
    print(cost)

solve()