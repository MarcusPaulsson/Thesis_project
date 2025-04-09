def solve():
  a, b, x = map(int, input().split())
  
  s = ""
  
  if a > b:
    start = 0
  else:
    start = 1
    
  
  if x % 2 == 0:
    
    for i in range(x):
      if i % 2 == 0:
        if start == 0:
          s += "0"
          a -= 1
        else:
          s += "1"
          b -= 1
      else:
        if start == 0:
          s += "1"
          b -= 1
        else:
          s += "0"
          a -= 1

    if start == 0:
      s += "0" * a
      s += "1" * b
    else:
      s += "1" * b
      s += "0" * a

  else:
    for i in range(x):
      if i % 2 == 0:
        if start == 0:
          s += "0"
          a -= 1
        else:
          s += "1"
          b -= 1
      else:
        if start == 0:
          s += "1"
          b -= 1
        else:
          s += "0"
          a -= 1
    
    if start == 0:
        s += "1" * b
        s += "0" * a
    else:
        s += "0" * a
        s += "1" * b
  print(s)
  

solve()