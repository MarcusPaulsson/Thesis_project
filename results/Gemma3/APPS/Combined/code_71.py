import math

def solve():
  a = int(input())
  
  if a == 1:
    print(1)
    return
  
  print(int(math.log2(a)))

solve()