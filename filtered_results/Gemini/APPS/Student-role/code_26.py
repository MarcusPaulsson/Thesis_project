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
expressions = ["x^y^z", "x^z^y", "(x^y)^z", "(x^z)^y", "y^x^z", "y^z^x", "(y^x)^z", "(y^z)^x", "z^x^y", "z^y^x", "(z^x)^y", "(z^y)^x"]

max_val = -1
max_index = -1

for i in range(len(values)):
    if values[i] > max_val:
        max_val = values[i]
        max_index = i

print(expressions[max_index])