def solve():
  x = float(input())
  
  a = int(x * 2.5)
  b = int((x * 2.5) + 1)
  
  a = min(max(a, 1), 10)
  b = min(max(b, 1), 10)
  
  print(a, b)

solve()