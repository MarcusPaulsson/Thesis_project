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
        
        temp_digits = digits[:]
        
        
        
        
        
        
        changes = 0
        
        
        
        
        
        
        
        
        
        
        
        if digits[0] != int(s1[0]):
          changes += 1
        if digits[1] != int(s1[1]):
          changes += 1
        if digits[2] != int(s1[2]):
          changes += 1
          
        if digits[3] != int(s2[0]):
          changes += 1
        if digits[4] != int(s2[1]):
          changes += 1
        if digits[5] != int(s2[2]):
          changes += 1
        
        
        
        
        
        
        ans = min(ans, changes)
        
  print(ans)
  
solve()