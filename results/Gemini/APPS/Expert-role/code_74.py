def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    distinct_chars = len(set(s))
    
    if distinct_chars == 1:
        total_subsequences = 0
        for i in range(n + 1):
            total_subsequences += 1
        if k > total_subsequences:
            print("-1")
            return
        
        cost = 0
        length = 0
        while k > 0:
            length += 1
            cost += min(k, 1) * (n - length)
            k -= min(k, 1)
        print(cost)
        return
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
    
    total_subsequences = 0
    for i in range(n + 1):
        total_subsequences += dp[n][i]

    if k > total_subsequences:
        print("-1")
        return
    
    ans = 0
    curr_len = n
    
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
    
    ans = 0
    curr_len = n
    
    used = [False] * n
    
    for i in range(n):
        for char_code in range(ord('a'), ord(s[i]) + 1):
            char = chr(char_code)
            
            count = 0
            for j in range(i):
                if not used[j] and s[j] == char:
                    count += 1
            
            if count > 0:
                continue
                
            temp_k = 0
            for length in range(0, n - i):
                temp_dp = [[0] * (n + 1) for _ in range(n + 1)]
                temp_dp[0][0] = 1
                
                for row in range(1, n - i):
                    for col in range(row + 1):
                        temp_dp[row][col] = temp_dp[row - 1][col]
                        if col > 0:
                            temp_dp[row][col] += temp_dp[row - 1][col - 1]
                
                temp_k += temp_dp[n-i-1][length]
            
            if k > temp_k:
                k -= temp_k
                ans += temp_k * (n - (n - i))
            else:
                ans += k * (n - (n - i))
                k = 0
                break
        if k == 0:
            break
        used[i] = True
            
    print(ans)
    
solve()