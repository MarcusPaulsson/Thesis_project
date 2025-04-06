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
        
  counts = []
  for i in range(n, -1, -1):
      counts.append(dp[n][i])

  total_cost = 0
  
  for i in range(len(counts)):
    if k > counts[i]:
        total_cost += counts[i] * (n - (len(counts) - 1 - i))
        k -= counts[i]
    else:
        total_cost += k * (n - (len(counts) - 1 - i))
        k = 0
        break
        
  if k > 0:
      print("-1")
  else:
      print(total_cost)

solve()