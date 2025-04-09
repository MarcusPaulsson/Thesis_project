def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    
    counts = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(26):
            counts[i][j] = counts[i-1][j]
        counts[i][ord(s[i-1]) - ord('a')] += 1

    dp2 = [[0] * (n + 1) for _ in range(n + 1)]
    dp2[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp2[i][0] = 1
            if j > 0:
                dp2[i][j] = dp2[i-1][j] + dp2[i-1][j-1]
            else:
                dp2[i][j] = dp2[i-1][j]
            
            
    
    subsequence_counts = []
    for i in range(n + 1):
        subsequence_counts.append(dp2[n][i])
    
    total_cost = 0
    
    if sum(subsequence_counts) < k:
        print("-1")
        return
    
    
    for length in range(n, -1, -1):
      
        if subsequence_counts[length] <= k:
            total_cost += subsequence_counts[length] * (n - length)
            k -= subsequence_counts[length]
        else:
            total_cost += k * (n - length)
            k = 0
            break
            
    print(total_cost)

solve()