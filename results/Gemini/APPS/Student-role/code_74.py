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

    
    counts = []
    for i in range(n + 1):
        counts.append(dp[n][i])

    counts.reverse()

    
    cost = 0
    total_subsequences = 0
    
    for i in range(len(counts)):
      
      if total_subsequences + counts[i] <= k:
        total_subsequences += counts[i]
        cost += counts[i] * (n - (len(counts) - 1 - i))
      else:
        needed = k - total_subsequences
        cost += needed * (n - (len(counts) - 1 - i))
        total_subsequences = k
        break
    
    if total_subsequences < k:
      print("-1")
    else:
      print(cost)

solve()