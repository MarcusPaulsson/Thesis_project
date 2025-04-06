def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    last_occurrence = {}
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            
            if s[i-1] in last_occurrence:
                prev_index = last_occurrence[s[i-1]]
                if j > 0:
                    dp[i][j] -= dp[prev_index - 1][j - 1]
        last_occurrence[s[i-1]] = i
        
    total_cost = 0
    current_len = n
    
    while k > 0:
        count = dp[n][current_len]
        
        if count >= k:
            total_cost += (n - current_len) * k
            k = 0
        else:
            total_cost += (n - current_len) * count
            k -= count
        
        current_len -= 1
        if current_len < 0 and k > 0:
            total_cost = -1
            break

    print(total_cost)

solve()