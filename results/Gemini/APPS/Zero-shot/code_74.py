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

  total_subsequences = sum(dp[n])

  if k > total_subsequences:
    print(-1)
    return

  dp = [[0] * (n + 1) for _ in range(n + 1)]
  dp[0][0] = 1

  for i in range(1, n + 1):
    for j in range(i + 1):
      dp[i][0] = 1
      if j > 0:
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][j] = min(dp[i][j], k)

  cost = 0
  for length in range(n, -1, -1):
    num_subsequences_of_length = dp[n][length]
    
    if k > num_subsequences_of_length:
      cost += (n - length) * num_subsequences_of_length
      k -= num_subsequences_of_length
    else:
      cost += (n - length) * k
      k = 0
      break

  print(cost)

solve()