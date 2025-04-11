def solve():
  a, b, x = map(int, input().split())

  if a > b:
    start = 0
    a -= 1
  else:
    start = 1
    b -= 1

  s = str(start)
  x -= 1

  while x > 0:
    if start == 0:
      if b > 0:
        s += '1'
        b -= 1
        start = 1
      else:
        s += '0'
        a -= 1
    else:
      if a > 0:
        s += '0'
        a -= 1
        start = 0
      else:
        s += '1'
        b -= 1
    x -= 1

  if start == 0:
    s += '0' * a
    s += '1' * b
  else:
    s += '1' * b
    s += '0' * a
  print(s)

solve()