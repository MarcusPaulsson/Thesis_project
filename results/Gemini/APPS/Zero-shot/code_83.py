def solve():
  x, y, a, b = map(int, input().split())
  
  if a + b == 0:
    if x == y:
      print(0)
    else:
      print(-1)
    return
      
  if (y - x) % (a + b) == 0:
    print((y - x) // (a + b))
  else:
    print(-1)

t = int(input())
for _ in range(t):
  solve()