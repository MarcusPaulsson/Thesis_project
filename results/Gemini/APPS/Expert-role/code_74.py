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
    
    total_subsequences = sum(dp[n])
    
    if total_subsequences < k:
        print("-1")
        return
    
    cost = 0
    current_length = n
    
    while k > 0:
        count = dp[n][current_length]
        
        if count >= k:
            cost += (n - current_length) * k
            k = 0
        else:
            cost += (n - current_length) * count
            k -= count
        n -= 1
        current_length -= 1
            
    print(cost)

solve()