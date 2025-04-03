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
            
    total_subsequences = sum(dp[n])
    
    if total_subsequences < k:
        print("-1")
        return

    ans = 0
    curr_len = n
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        last_occurrence = {}
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j]
            dp[i][j] += dp[i-1][j-1]
            
            if s[i-1] in last_occurrence:
                dp[i][j] -= dp[last_occurrence[s[i-1]] - 1][j-1]
        
        last_occurrence[s[i-1]] = i
    
    curr_len = n
    
    for length in range(n, -1, -1):
        num_subsequences = dp[n][length]
        
        if k > num_subsequences:
            ans += (n - length) * num_subsequences
            k -= num_subsequences
        else:
            ans += (n - length) * k
            k = 0
            break
    
    print(ans)

solve()