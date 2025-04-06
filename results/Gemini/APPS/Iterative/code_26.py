import math

x, y, z = map(float, input().split())

a1 = y**z * math.log(x)
a2 = z**y * math.log(x)
a3 = y * z * math.log(x)
a4 = z * y * math.log(x)
a5 = x**z * math.log(y)
a6 = z**x * math.log(y)
a7 = x * z * math.log(y)
a8 = z * x * math.log(y)
a9 = x**y * math.log(z)
a10 = y**x * math.log(z)
a11 = x * y * math.log(z)
a12 = y * x * math.log(z)

mx = a1
ans = "x^y^z"
if a2 > mx:
    mx = a2
    ans = "x^z^y"
if a3 > mx:
    mx = a3
    ans = "(x^y)^z"
if a4 > mx:
    mx = a4
    ans = "(x^z)^y"
if a5 > mx:
    mx = a5
    ans = "y^x^z"
if a6 > mx:
    mx = a6
    ans = "y^z^x"
if a7 > mx:
    mx = a7
    ans = "(y^x)^z"
if a8 > mx:
    mx = a8
    ans = "(y^z)^x"
if a9 > mx:
    mx = a9
    ans = "z^x^y"
if a10 > mx:
    mx = a10
    ans = "z^y^x"
if a11 > mx:
    mx = a11
    ans = "(z^x)^y"
if a12 > mx:
    mx = a12
    ans = "(z^y)^x"

print(ans)