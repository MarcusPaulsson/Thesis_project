def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
    counts = [0] * (n + 1)
    for i in range(n + 1):
        counts[i] = dp[n][i]
    
    
    distinct_counts = [0] * (n + 1)
    distinct_counts[0] = 1
    
    for i in range(1, n + 1):
        distinct_counts[i] = 0
        used = set()
        for j in range(n):
            if s[j] not in used:
                used.add(s[j])
                if i > 0:
                    distinct_counts[i] += dp[n - j - 1][i - 1]
                    distinct_counts[i] = min(distinct_counts[i], k)
    
    
    cost = 0
    for i in range(n, -1, -1):
        if k > distinct_counts[i]:
            cost += (n - i) * distinct_counts[i]
            k -= distinct_counts[i]
        else:
            cost += (n - i) * k
            k = 0
            break
            
    if k > 0:
        print("-1")
    else:
        print(cost)

solve()