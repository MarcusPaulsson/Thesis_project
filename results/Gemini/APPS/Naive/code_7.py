def solve():
  n, m = map(int, input().split())

  low = 0
  high = 2 * 10**9

  ans = -1

  while low <= high:
    mid = (low + high) // 2
    
    total_sparrows = (mid * (mid + 1)) // 2
    
    if total_sparrows >= n + (mid * m):
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
      
  print(ans)

solve()