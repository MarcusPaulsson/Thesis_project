def solve():
  n, m = map(int, input().split())
  
  l, r = 0, 2 * 10**9
  ans = r
  
  while l <= r:
    mid = (l + r) // 2
    
    total_sparrows = mid * (mid + 1) // 2
    
    if n + mid * m >= total_sparrows:
      ans = mid
      r = mid - 1
    else:
      l = mid + 1
      
  print(ans)

solve()