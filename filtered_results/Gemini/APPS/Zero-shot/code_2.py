def solve():
  n = int(input())
  s = str(n)
  l = len(s)
  first_digit = int(s[0])
  
  next_lucky = (first_digit + 1) * (10**(l-1))
  
  print(next_lucky - n)

solve()