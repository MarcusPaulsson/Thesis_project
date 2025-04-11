def solve():
  x = float(input())
  
  for a in range(1, 11):
    for b in range(1, 11):
      if abs(a**0.5 + b**0.5 - x) < 1e-7:
        print(a, b)
        return

solve()