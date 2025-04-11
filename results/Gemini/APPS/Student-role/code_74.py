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
    
    total_cost = 0
    
    for length in range(n, -1, -1):
        count = dp[n][length]
        
        if k > count:
            total_cost += (n - length) * count
            k -= count
        else:
            total_cost += (n - length) * k
            k = 0
            break
    
    if k > 0:
        print("-1")
    else:
        print(total_cost)

solve()