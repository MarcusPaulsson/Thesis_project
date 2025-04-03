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
    
    ans = 0
    len_sub = n
    while k > 0 and len_sub >= 0:
        num_subs = dp[n][len_sub]
        
        if num_subs <= k:
            k -= num_subs
            ans += (n - len_sub) * num_subs
        else:
            ans += (n - len_sub) * k
            k = 0
            break
        
        len_sub -= 1
        n -= 1

    if k > 0:
        print(-1)
    else:
        print(ans)

solve()