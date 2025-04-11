d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = (d - 1) // k
    
    if num_breaks * t + d * a < k * a + (num_breaks * k) * a + (d - num_breaks * k) * b:
        print(num_breaks * t + d * a)
    else:
        print(k * a + (num_breaks * t) + (d - k - num_breaks * (k - k)) * b)
    
    
    if (d // k) >= 1:
        
        if (d // k) * k != d:
            print((d // k) * (k * a + t) + (d % k) * a if (d // k) * (k * a + t) + (d % k) * a < (k * a) + (t * (d // k -1 + 1)) + ((d - (k + (d // k - 1 + 1) * (k-k)))) * b else (k * a) + (t * (d // k -1 + 1)) + ((d - (k + (d // k - 1 + 1) * (k-k)))) * b)
            
        else:
            print((d // k-1) * (k * a + t) + (k * a) if (d // k-1) * (k * a + t) + (k * a) < (k * a) + (t * (d // k -1)) + ((d - (k + (d // k - 1) * (k-k)))) * b else (k * a) + (t * (d // k -1)) + ((d - (k + (d // k - 1) * (k-k)))) * b)

    else:
            print(d * a)

    if k * a + t > k * b:
      print(k * a + (d-k) * b)
    
    else:
        num_k = d // k
        rem = d % k
        
        print(k*a*num_k + t*(num_k-1) + rem*a) if num_k != 0 else print(d*a)