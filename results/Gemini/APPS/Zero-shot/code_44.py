d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if k * a + t >= k * b:
    print(k * a + (d - k) * b)
  else:
    num_breaks = (d - 1) // k
    
    total_time = num_breaks * (k * a + t)
    
    remaining_distance = d - num_breaks * k
    
    total_time += remaining_distance * a
    
    print(total_time)