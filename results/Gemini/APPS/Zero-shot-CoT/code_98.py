def solve():
  c, m, x = map(int, input().split())
  
  low = 0
  high = min(c, m, x)
  ans = 0
  
  while low <= high:
    mid = (low + high) // 2
    
    if c >= mid and m >= mid and x >= mid:
      ans = mid
      low = mid + 1
    else:
      high = mid - 1
      
  
  remaining_c = c - ans
  remaining_m = m - ans
  remaining_x = x - ans
  
  
  
  
  
  ans += min(remaining_c, remaining_m, (remaining_c + remaining_m) // 3)
  
  print(ans)

q = int(input())
for _ in range(q):
  solve()