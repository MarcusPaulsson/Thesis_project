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
        
        counts = {}
        for l in range(i):
          if s[l] in counts:
            counts[s[l]] +=1
          else:
            counts[s[l]] = 1
    
    
    counts = {}
    
    
    combinations = [[0] * (n + 1) for _ in range(n + 1)]
    combinations[0][0] = 1
    
    for i in range(1, n + 1):
      for j in range(i + 1):
        combinations[i][0] = 1
        if j > 0:
          combinations[i][j] = combinations[i-1][j] + combinations[i-1][j-1]
          
    
    subsequence_counts = [0] * (n + 1)
    
    combinations = [[0] * (n + 1) for _ in range(n + 1)]
    combinations[0][0] = 1
    
    for i in range(1, n + 1):
      for j in range(i + 1):
        combinations[i][0] = 1
        if j > 0:
          combinations[i][j] = combinations[i-1][j] + combinations[i-1][j-1]
    
    
    subsequence_counts = [0] * (n + 1)
    
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    
    
    subsequence_counts = [0] * (n + 1)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        counts = {}
        for char in s[:i]:
            counts[char] = counts.get(char, 0) + 1
        
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                if s[i-1] in counts and counts[s[i-1]] > 1:
                   
                    first_occurrence = -1
                    for l in range(i-1):
                        if s[l] == s[i-1]:
                            first_occurrence = l
                            break
                   
                    if first_occurrence != -1:
                        dp[i][j] -= dp[first_occurrence][j-1]
                        if dp[i][j] < 0:
                            dp[i][j] = max(0, dp[i][j])

    total_cost = 0
    
    for length in range(n, -1, -1):
        if dp[n][length] <= k:
            total_cost += (n - length) * dp[n][length]
            k -= dp[n][length]
        else:
            total_cost += (n - length) * k
            k = 0
            break

    if k > 0:
      print("-1")
    else:
      print(total_cost)

solve()