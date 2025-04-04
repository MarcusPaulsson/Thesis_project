x, y, z = map(float, input().split())
a = [x**y**z, x**z**y, (x**y)**z, (x**z)**y, y**x**z, y**z**x, (y**x)**z, (y**z)**x, z**x**y, z**y**x, (z**x)**y, (z**y)**x]
c = a.index(max(a))
if c == 0:
    print("x^y^z")
elif c == 1:
    print("x^z^y")
elif c == 2:
    print("(x^y)^z")
elif c == 3:
    print("(x^z)^y")
elif c == 4:
    print("y^x^z")
elif c == 5:
    print("y^z^x")
elif c == 6:
    print("(y^x)^z")
elif c == 7:
    print("(y^z)^x")
elif c == 8:
    print("z^x^y")
elif c == 9:
    print("z^y^x")
elif c == 10:
    print("(z^x)^y")
elif c == 11:
    print("(z^y)^x")