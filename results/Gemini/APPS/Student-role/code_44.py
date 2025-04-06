d, k, a, b, t = map(int, input().split())

if d <= k:
  print(d * a)
else:
  if a * k + t >= b * k:
    print(k * a + (d - k) * b)
  else:
    num_breaks = d // k
    rem = d % k
    
    if rem == 0:
      print(num_breaks * k * a + (num_breaks - 1) * t)
    else:
      
      print(num_breaks * k * a + num_breaks * t + rem * min(a,b))
      
      ans1 = num_breaks * k * a + (num_breaks) * t + rem * a
      ans2 = k*a + (d-k) * b
      
      if num_breaks >0:
          ans2 = (num_breaks) * (k*a + t) + (d - (num_breaks) * k) * b
          ans1 = (num_breaks) * (k*a + t) + (d - (num_breaks) * k) * a
          
          print(min(ans2,num_breaks * (k*a+t) + (d - num_breaks * k) * b ))
      else:
          print(min(k*a + (d-k)*b, d*b ))

      print(min(num_breaks * (k*a+t) + (d - num_breaks * k) * b , num_breaks * (k*a+t) + (d - num_breaks * k) * a))
      
      print(min(num_breaks * k * a + num_breaks * t + rem * a , num_breaks * k * a + num_breaks * t + rem * b))
      print(num_breaks * k * a + num_breaks * t + rem * min(a,b))
      
      print(min(num_breaks * (k*a+t) + (d - num_breaks * k) * a, num_breaks * (k*a+t) + (d - num_breaks * k) * b))
      
      
      
      ans=0
      
      if d <= k:
          ans = d*a
      else:
          ans = k*a
          d-=k
          
          ans += min(d*b , (d//k) * (k*a + t) + (d%k) * a + t )
          
          
          
      #print(min(k*a + (d-k)*b, num_breaks * (k*a+t) + rem*a + t if rem > 0 else 0))
      
      
      #print(num_breaks * (k*a+t) + rem * b if rem > 0 else 0)
      
      print(min( num_breaks * (k*a + t) + rem*b, (num_breaks) * (k * a + t) + rem * a))