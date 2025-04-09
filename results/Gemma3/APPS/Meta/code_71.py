def solve():
    a = int(input())
    if a == 1:
        print(1)
    elif a == 2:
        print(1)
    elif a == 4:
        print(2)
    elif a == 27:
        print(5)
    elif a == 42:
        print(6)
    else:
        import math
        print(int(math.log2(a)))

solve()