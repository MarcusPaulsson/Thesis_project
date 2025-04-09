d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = (d - 1) // k
    
    print(min(d * a + num_breaks * t, k * a + t + (d - k) * b, num_breaks * (k*a + t) + (d - num_breaks * k) * a if d - num_breaks*k <= k else num_breaks * (k*a + t) + (d - num_breaks*k) *b))