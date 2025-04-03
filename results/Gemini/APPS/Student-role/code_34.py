def solve():
  n = int(input())
  
  segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
  
  if n % 2 == 0:
    print("1" * (n // 2))
  else:
    print("7" + "1" * ((n - 3) // 2))

t = int(input())
for _ in range(t):
  solve()