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
  
  if k > total_subsequences:
    print(-1)
    return

  dp = [[0] * (n + 1) for _ in range(n + 1)]
  dp[0][0] = 1
  
  for i in range(1, n + 1):
    for j in range(i + 1):
      dp[i][j] = dp[i - 1][j]
      if j > 0:
        dp[i][j] += dp[i - 1][j - 1]

  ans = 0
  curr_len = n
  
  while k > 0:
      
    num_subsequences_len_curr_len = dp[n][curr_len] if curr_len <= n else 0
    
    if k <= num_subsequences_len_curr_len:
      ans += (n - curr_len) * k
      k = 0
    else:
      ans += (n - curr_len) * num_subsequences_len_curr_len
      k -= num_subsequences_len_curr_len

    curr_len -= 1
    
  print(ans)

solve()