import math

a = int(input())
if a == 1:
  print(1)
else:
  print(int(math.ceil(math.log2(a))))