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
    
    if a1 == m:
        print("x^y^z")
    elif a2 == m:
        print("x^z^y")
    elif a3 == m:
        print("(x^y)^z")
    elif a4 == m:
        print("(x^z)^y")
    elif a5 == m:
        print("y^x^z")
    elif a6 == m:
        print("y^z^x")
    elif a7 == m:
        print("(y^x)^z")
    elif a8 == m:
        print("(y^z)^x")
    elif a9 == m:
        print("z^x^y")
    elif a10 == m:
        print("z^y^x")
    elif a11 == m:
        print("(z^x)^y")
    else:
        print("(z^y)^x")

solve()