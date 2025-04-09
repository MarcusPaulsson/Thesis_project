n, m = map(int, input().split())

left = 0
right = 2 * 10**9

ans = right

while left <= right:
  mid = (left + right) // 2
  
  total_sparrows = mid * (mid + 1) // 2
  
  full_barns = total_sparrows // n
  
  remaining_sparrows = total_sparrows % n
  
  
  
  grains_added = mid * m
  
  
  total_grains = n + grains_added
  
  
  grains_eaten = total_sparrows
  
  
  if n + grains_added <= grains_eaten:
    ans = mid
    right = mid - 1
  else:
    
    
    
    if n + (mid * m) - (mid * (mid + 1) // 2) <= 0:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1

print(ans)