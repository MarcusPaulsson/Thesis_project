n, m = map(int, input().split())

low = 0
high = 2 * 10**9

ans = -1

while low <= high:
  mid = (low + high) // 2
  
  total_grain = n + mid * m
  
  if total_grain >= mid * (mid + 1) // 2:
    ans = mid
    high = mid - 1
  else:
    low = mid + 1
    
print(ans)