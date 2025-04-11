d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = d // k
    remaining = d % k
    
    time = num_breaks * (k * a + t)
    
    if remaining > 0:
      if remaining * a + t < remaining * b:
        time += remaining * a
      else:
        time -= t
        time += remaining * b
    else:
      time -= t
      
    print(time)