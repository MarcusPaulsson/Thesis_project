d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = (d // k)
    remaining = d % k
    
    time = num_breaks * (a * k + t)
    
    if remaining > 0:
      time += min(remaining * a, remaining * b + t)
    else:
      time -= t

    print(time)