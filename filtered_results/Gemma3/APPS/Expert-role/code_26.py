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
    
    a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
    
    m = max(a)
    
    c = a.index(m) + 1
    
    if c == 1:
        print("x^y^z")
    elif c == 2:
        print("x^z^y")
    elif c == 3:
        print("(x^y)^z")
    elif c == 4:
        print("(x^z)^y")
    elif c == 5:
        print("y^x^z")
    elif c == 6:
        print("y^z^x")
    elif c == 7:
        print("(y^x)^z")
    elif c == 8:
        print("(y^z)^x")
    elif c == 9:
        print("z^x^y")
    elif c == 10:
        print("z^y^x")
    elif c == 11:
        print("(z^x)^y")
    else:
        print("(z^y)^x")

solve()