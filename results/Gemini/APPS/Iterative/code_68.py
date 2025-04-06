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
            
    
    distinct_dp = [[0] * (n + 1) for _ in range(n + 1)]
    distinct_dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            distinct_dp[i][j] = distinct_dp[i-1][j]
            if j > 0:
                distinct_dp[i][j] += distinct_dp[i-1][j-1]
            distinct_dp[i][j] = min(distinct_dp[i][j], k)
            
        for l in range(i):
            if s[l] == s[i-1]:
                for j in range(i + 1):
                    if j > 0:
                        distinct_dp[i][j] -= distinct_dp[l][j-1]
                        distinct_dp[i][j] = max(0, distinct_dp[i][j])
    
    
    total_cost = 0
    
    for length in range(n, -1, -1):
        
        if distinct_dp[n][length] > 0:
            
            take = min(k, distinct_dp[n][length])
            k -= take
            total_cost += take * (n - length)
            
            if k == 0:
                print(total_cost)
                return


    print(-1)

solve()