def solve():
  c, m, x = map(int, input().split())
  
  low = 0
  high = min(c, m, x)
  ans = 0
  
  while low <= high:
    mid = (low + high) // 2
    
    if c >= mid and m >= mid and x >= mid:
      if c - mid + m - mid + x - mid >= 0:
        ans = mid
        low = mid + 1
      else:
        high = mid - 1
    else:
      high = mid - 1
  
  print(ans)

q = int(input())
for _ in range(q):
  solve()