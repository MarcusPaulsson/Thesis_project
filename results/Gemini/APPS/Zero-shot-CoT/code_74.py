def solve():
  n, k = map(int, input().split())
  s = input()

  dp = [[0] * (n + 1) for _ in range(n + 1)]
  dp[0][0] = 1

  for i in range(1, n + 1):
    for j in range(i + 1):
      dp[i][j] = dp[i - 1][j]
      if j > 0:
        dp[i][j] += dp[i - 1][j - 1]

  
  counts = [0] * (n + 1)
  for i in range(n + 1):
    counts[i] = dp[n][i]
    
  total_cost = 0
  current_size = 0
  
  for i in range(n, -1, -1):
      
      if current_size + counts[i] <= k:
          current_size += counts[i]
          total_cost += (n - i) * counts[i]
      else:
          total_cost += (n-i) * (k - current_size)
          current_size = k
          break

  if current_size < k:
      print("-1")
  else:
      print(total_cost)

solve()