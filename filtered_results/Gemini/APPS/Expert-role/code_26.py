def solve():
    x, y, z = map(float, input().split())

    a1 = x**(y**z)
    a2 = x**(z**y)
    a3 = (x**y)**z
    a4 = (x**z)**y
    a5 = y**(x**z)
    a6 = y**(z**x)
    a7 = (y**x)**z
    a8 = (y**z)**x
    a9 = z**(x**y)
    a10 = z**(y**x)
    a11 = (z**x)**y
    a12 = (z**y)**x

    values = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
    
    max_val = max(values)
    
    if values[0] == max_val:
        print("x^y^z")
    elif values[1] == max_val:
        print("x^z^y")
    elif values[2] == max_val:
        print("(x^y)^z")
    elif values[3] == max_val:
        print("(x^z)^y")
    elif values[4] == max_val:
        print("y^x^z")
    elif values[5] == max_val:
        print("y^z^x")
    elif values[6] == max_val:
        print("(y^x)^z")
    elif values[7] == max_val:
        print("(y^z)^x")
    elif values[8] == max_val:
        print("z^x^y")
    elif values[9] == max_val:
        print("z^y^x")
    elif values[10] == max_val:
        print("(z^x)^y")
    else:
        print("(z^y)^x")

solve()