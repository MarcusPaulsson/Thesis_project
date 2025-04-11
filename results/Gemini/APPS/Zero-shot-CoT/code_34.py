def solve():
  n, a, b = map(int, input().split())
  
  ans = 0
  for i in range(1, n):
    if i >= 1 and i < n:
      plate_a = i
      plate_b = n - i
      
      x = min(a // plate_a, b // plate_b)
      ans = max(ans, x)
  print(ans)
  
solve()