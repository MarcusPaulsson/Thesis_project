def solve():
  n, m = map(int, input().split())

  low = 0
  high = 2 * 10**9
  ans = -1

  while low <= high:
    mid = (low + high) // 2
    total_sparrows = mid * (mid + 1) // 2

    if total_sparrows >= n:
      grains_left = n - (total_sparrows % n)
      if grains_left <= 0:
          ans = mid
          high = mid - 1
      else:
          low = mid + 1
    else:
      grains_left = n - total_sparrows
      
      if grains_left % m == 0:
        days_needed = grains_left // m
      else:
        days_needed = grains_left // m + 1
      
      if mid >= days_needed:
        ans = mid
        high = mid - 1
      else:
        low = mid + 1

  print(ans)

solve()