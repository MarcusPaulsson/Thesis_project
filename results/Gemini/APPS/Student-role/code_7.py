n, m = map(int, input().split())

low = 0
high = 2 * 10**9
ans = high

while low <= high:
    mid = (low + high) // 2
    
    total_sparrows = mid * (mid + 1) // 2
    
    grains_eaten = 0
    
    if total_sparrows >= n:
      grains_eaten = n
    else:
      grains_eaten = total_sparrows
      
    
    total_added = 0
    
    num_cycles = n // m
    
    if num_cycles >= mid:
        total_added = mid * m
    else:
        total_added = num_cycles * m
        
    
    
    
    current_grains = n + total_added - grains_eaten
    
    if current_grains <= 0:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)