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
    
    
    unique_counts = [0] * (n + 1)
    unique_counts[0] = 1
    
    for i in range(1, n + 1):
        unique_counts[i] = 0
        
        last_occurrence = {}
        
        dp_unique = [[0] * (n + 1) for _ in range(n + 1)]
        dp_unique[0][0] = 1
        
        for i_idx in range(1, n + 1):
            for j_idx in range(i_idx + 1):
                dp_unique[i_idx][0] = 1
                if j_idx > 0:
                    dp_unique[i_idx][j_idx] = dp_unique[i_idx-1][j_idx-1] + dp_unique[i_idx-1][j_idx]
                    
                    if s[i_idx-1] in last_occurrence:
                        prev_idx = last_occurrence[s[i_idx-1]]
                        dp_unique[i_idx][j_idx] -= dp_unique[prev_idx-1][j_idx-1] if prev_idx > 0 else 0
            last_occurrence[s[i_idx-1]] = i_idx
        
        for i_idx in range(n+1):
            unique_counts[i_idx] = dp_unique[n][i_idx]
            
    
    
    cost = 0
    
    for length in range(n, -1, -1):
        take = min(k, unique_counts[length])
        cost += (n - length) * take
        k -= take
        
        if k == 0:
            print(cost)
            return
    
    print(-1)

solve()