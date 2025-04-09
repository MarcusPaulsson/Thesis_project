import math

def solve():
    x, y, z = map(float, input().split())

    a1 = x ** (y ** z)
    a2 = x ** (z ** y)
    a3 = (x ** y) ** z
    a4 = (x ** z) ** y
    a5 = y ** (x ** z)
    a6 = y ** (z ** x)
    a7 = (y ** x) ** z
    a8 = (y ** z) ** x
    a9 = z ** (x ** y)
    a10 = z ** (y ** x)
    a11 = (z ** x) ** y
    a12 = (z ** y) ** x

    values = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
    
    max_val = max(values)
    max_index = values.index(max_val) + 1

    if max_index == 1:
        print("x^y^z")
    elif max_index == 2:
        print("x^z^y")
    elif max_index == 3:
        print("(x^y)^z")
    elif max_index == 4:
        print("(x^z)^y")
    elif max_index == 5:
        print("y^x^z")
    elif max_index == 6:
        print("y^z^x")
    elif max_index == 7:
        print("(y^x)^z")
    elif max_index == 8:
        print("(y^z)^x")
    elif max_index == 9:
        print("z^x^y")
    elif max_index == 10:
        print("z^y^x")
    elif max_index == 11:
        print("(z^x)^y")
    elif max_index == 12:
        print("(z^y)^x")

solve()