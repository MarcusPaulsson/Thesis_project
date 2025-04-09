def solve():
  s = input()
  t = input()
  n = len(s)
  m = len(t)
  
  ans = 0
  for i in range(n + 1):
    for j in range(i, n + 1):
      temp_s = ""
      if i > 0:
        temp_s += s[:i]
      if j < n:
        temp_s += s[j:]
        
      
      ti = 0
      tsi = 0
      
      possible = True
      while ti < m and tsi < len(temp_s):
        if t[ti] == temp_s[tsi]:
          ti += 1
          tsi += 1
        else:
          tsi += 1
      
      if ti == m:
        ans = max(ans, j - i)
        
  print(ans)

solve()