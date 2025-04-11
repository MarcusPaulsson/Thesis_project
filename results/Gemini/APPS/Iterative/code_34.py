def solve():
  n, a, b = map(int, input().split())
  
  ans = 0
  for i in range(1, n):
    if i >= n:
      continue
    
    ans = max(ans, min(a // i, b // (n - i)))
  
  print(ans)

solve()