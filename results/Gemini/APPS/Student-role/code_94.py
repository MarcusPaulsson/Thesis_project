def solve():
  a, b, x = map(int, input().split())
  
  if a > b:
    start = 0
    a_char = '0'
    b_char = '1'
  else:
    start = 1
    a_char = '1'
    b_char = '0'
    
  res = ""
  
  if start == 0:
    res += a_char
    a -= 1
  else:
    res += b_char
    b -= 1
    
  x -= 1
  
  while x > 0:
    if res[-1] == a_char:
      res += b_char
      b -= 1
    else:
      res += a_char
      a -= 1
    x -= 1
    
  if res[-1] == a_char:
    res += b_char * b
    res += a_char * a
  else:
    res += a_char * a
    res += b_char * b
    
  print(res)
  
solve()