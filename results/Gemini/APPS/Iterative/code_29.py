def solve():
  s = input()
  digits = [int(c) for c in s]
  
  ans = 6
  
  for i in range(1000):
    for j in range(1000):
      
      temp_digits = []
      
      temp_digits.append(i // 100)
      temp_digits.append((i % 100) // 10)
      temp_digits.append(i % 10)
      
      temp_digits.append(j // 100)
      temp_digits.append((j % 100) // 10)
      temp_digits.append(j % 10)
      
      diff = 0
      for k in range(6):
        if temp_digits[k] != digits[k]:
          diff += 1
          
      if sum(temp_digits[:3]) == sum(temp_digits[3:]):
        ans = min(ans, diff)
      
  print(ans)

solve()