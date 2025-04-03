def solve():
  n = int(input())
  s = input()
  
  ans = n
  
  for i in range(1, n // 2 + 1):
    prefix = s[:i]
    if s[:2*i] == prefix + prefix:
      ans = min(ans, i + 1 + (n - 2*i))
  
  print(ans)

solve()