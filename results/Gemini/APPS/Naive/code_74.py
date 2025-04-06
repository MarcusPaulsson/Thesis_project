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
      
  total_subsequences = sum(dp[n])
  
  if total_subsequences < k:
    print("-1")
    return
  
  cost = 0
  length = n
  
  while k > 0:
    num_subsequences_of_length = dp[n][length]
    
    if num_subsequences_of_length <= k:
      cost += num_subsequences_of_length * (n - length)
      k -= num_subsequences_of_length
      length -= 1
    else:
      cost += k * (n - length)
      k = 0
      
  print(cost)
  

solve()