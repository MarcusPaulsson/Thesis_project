d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = d // k
    remainder = d % k
    
    time = num_breaks * (k * a + t)
    
    if remainder > 0:
      time += min(remainder * a, remainder * b + t)
    else:
      time -= t
    
    print(time)