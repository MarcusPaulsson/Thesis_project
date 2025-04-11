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
    
    total_subsequences = sum(dp[n])
    
    if total_subsequences < k:
        print("-1")
        return
    
    cost = 0
    for length in range(n, -1, -1):
        num_subsequences_of_length = dp[n][length]
        
        take = min(num_subsequences_of_length, k)
        cost += (n - length) * take
        k -= take
        
        if k == 0:
            break
    
    print(cost)

solve()