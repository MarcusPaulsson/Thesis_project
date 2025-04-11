def solve():
  s = input()
  digits = [int(c) for c in s]
  
  ans = 6
  for i in range(1000):
    s1 = str(i).zfill(3)
    sum1 = sum(int(c) for c in s1)
    
    for j in range(1000):
      s2 = str(j).zfill(3)
      sum2 = sum(int(c) for c in s2)
      
      if sum1 == sum2:
        
        temp_digits = [int(c) for c in s1 + s2]
        
        diff = 0
        for k in range(6):
          if digits[k] != temp_digits[k]:
            diff += 1
        ans = min(ans, diff)
  print(ans)

solve()