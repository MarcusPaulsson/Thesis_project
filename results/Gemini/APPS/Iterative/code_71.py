import math

a = int(input())
if a == 1:
    print(0)
else:
    print(math.ceil(math.log2(a)))