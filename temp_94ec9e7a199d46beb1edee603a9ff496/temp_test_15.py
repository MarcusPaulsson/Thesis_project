def solve():
  a, b, x, y = map(int, input().split())
  
  ans = 0
  
  # Case 1: Window is to the right of the dead pixel
  width = a - x - 1
  height = b
  ans = max(ans, width * height)
  
  # Case 2: Window is to the left of the dead pixel
  width = x
  height = b
  ans = max(ans, width * height)
  
  # Case 3: Window is below the dead pixel
  width = a
  height = y
  ans = max(ans, width * height)
  
  # Case 4: Window is above the dead pixel
  width = a
  height = b - y - 1
  ans = max(ans, width * height)
  
  print(ans)

t = int(input())
for _ in range(t):
  solve()