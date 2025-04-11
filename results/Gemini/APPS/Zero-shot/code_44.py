d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  cost = k * a
  remaining = d - k
  
  if t + k * a < k * b:
    num_breaks = remaining // k
    cost += num_breaks * (t + k * a)
    remaining %= k
    
    if t + remaining * a < remaining * b:
      cost += t + remaining * a
    else:
      cost += remaining * b
  else:
    cost += remaining * b
    
  print(cost)