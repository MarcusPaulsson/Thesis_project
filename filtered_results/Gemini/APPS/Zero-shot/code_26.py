import math

x, y, z = map(float, input().split())

a1 = y**z * math.log(x) if x > 0 else -float('inf')
a2 = z**y * math.log(x) if x > 0 else -float('inf')
a3 = y * z * math.log(x) if x > 0 else -float('inf')
a4 = z * y * math.log(x) if x > 0 else -float('inf')
a5 = x**z * math.log(y) if y > 0 else -float('inf')
a6 = z**x * math.log(y) if y > 0 else -float('inf')
a7 = x * z * math.log(y) if y > 0 else -float('inf')
a8 = z * x * math.log(y) if y > 0 else -float('inf')
a9 = x**y * math.log(z) if z > 0 else -float('inf')
a10 = y**x * math.log(z) if z > 0 else -float('inf')
a11 = x * y * math.log(z) if z > 0 else -float('inf')
a12 = y * x * math.log(z) if z > 0 else -float('inf')

values = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
max_val = max(values)
index = values.index(max_val)

if index == 0:
    print("x^y^z")
elif index == 1:
    print("x^z^y")
elif index == 2:
    print("(x^y)^z")
elif index == 3:
    print("(x^z)^y")
elif index == 4:
    print("y^x^z")
elif index == 5:
    print("y^z^x")
elif index == 6:
    print("(y^x)^z")
elif index == 7:
    print("(y^z)^x")
elif index == 8:
    print("z^x^y")
elif index == 9:
    print("z^y^x")
elif index == 10:
    print("(z^x)^y")
elif index == 11:
    print("(z^y)^x")