def solve():
  n, a, b = map(int, input().split())
  
  max_x = 0
  for i in range(1, n):
    if i > a or n - i > b:
        continue
    
    x1 = a // i
    x2 = b // (n - i)
    
    max_x = max(max_x, min(x1, x2))
  
  print(max_x)

solve()