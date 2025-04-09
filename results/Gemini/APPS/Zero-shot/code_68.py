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

  counts = [0] * (n + 1)
  for i in range(n + 1):
    counts[i] = dp[n][i]
  
  ans = 0
  curr_len = n
  
  while k > 0 and curr_len >= 0:
    take = min(k, counts[curr_len])
    ans += (n - curr_len) * take
    k -= take
    curr_len -= 1
  
  if k > 0:
    print(-1)
  else:
    print(ans)

solve()