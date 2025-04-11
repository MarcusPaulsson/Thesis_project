d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  cost = k * a
  remaining_distance = d - k
  
  if t + k * a < k * b:
    num_breaks = remaining_distance // k
    cost += num_breaks * (t + k * a)
    remaining_distance %= k
    
    if remaining_distance > 0:
      cost += min(t + remaining_distance * a, remaining_distance * b)
  else:
    cost += remaining_distance * b
    
  print(cost)