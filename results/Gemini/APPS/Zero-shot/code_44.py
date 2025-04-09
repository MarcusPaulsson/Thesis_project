d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if k * a + t >= k * b:
    print(k * a + (d - k) * b)
  else:
    num_breaks = (d - 1) // k
    
    if num_breaks * t + d * a < k * a + (d - k) * b + (num_breaks - 1 )*t:
        print(num_breaks * t + d * a)
    else:
        print(k * a + (d - k) * b + num_breaks * t)