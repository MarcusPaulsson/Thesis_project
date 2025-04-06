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

    max_val = a1
    max_index = 1

    if a2 > max_val:
        max_val = a2
        max_index = 2
    
    if a3 > max_val:
        max_val = a3
        max_index = 3

    if a4 > max_val:
        max_val = a4
        max_index = 4
        
    if a5 > max_val:
        max_val = a5
        max_index = 5
    
    if a6 > max_val:
        max_val = a6
        max_index = 6
        
    if a7 > max_val:
        max_val = a7
        max_index = 7

    if a8 > max_val:
        max_val = a8
        max_index = 8
        
    if a9 > max_val:
        max_val = a9
        max_index = 9

    if a10 > max_val:
        max_val = a10
        max_index = 10
    
    if a11 > max_val:
        max_val = a11
        max_index = 11

    if a12 > max_val:
        max_val = a12
        max_index = 12
        
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