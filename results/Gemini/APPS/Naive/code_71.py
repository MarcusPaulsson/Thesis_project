import math

def solve():
    a = int(input())
    if a == 1:
        print(1)
    else:
        print(math.ceil(math.log(a, 2)))

solve()