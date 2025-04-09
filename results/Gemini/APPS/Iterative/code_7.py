n, m = map(int, input().split())

left = 0
right = 2 * 10**9

ans = -1

while left <= right:
  mid = (left + right) // 2
  
  total_sparrows = mid * (mid + 1) // 2
  
  
  if n + mid * m >= total_sparrows:
    ans = mid
    right = mid - 1
  else:
    left = mid + 1

print(ans)