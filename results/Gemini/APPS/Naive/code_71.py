import math

def solve():
  a = int(input())
  if a == 1:
    print(1)
    return

  print(math.ceil(math.log(a, 2)))

solve()