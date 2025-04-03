x, y, z = map(float, input().split())

a1 = y**z * (x > 1) + z**y * (x <= 1)
a2 = z**y * (x > 1) + y**z * (x <= 1)
a3 = y * z
a4 = z * y
a5 = x**z * (y > 1) + z**x * (y <= 1)
a6 = z**x * (y > 1) + x**z * (y <= 1)
a7 = x * z
a8 = z * x
a9 = x**y * (z > 1) + y**x * (z <= 1)
a10 = y**x * (z > 1) + x**y * (z <= 1)
a11 = x * y
a12 = y * x

vals = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
results = ["x^y^z", "x^z^y", "(x^y)^z", "(x^z)^y", "y^x^z", "y^z^x", "(y^x)^z", "(y^z)^x", "z^x^y", "z^y^x", "(z^x)^y", "(z^y)^x"]

max_val = -float('inf')
max_index = -1

for i in range(12):
  if x > 0 and y > 0 and z > 0:
    if i < 2:
      val = x ** vals[i]
    elif i < 4:
      val = x ** vals[i]
    elif i < 6:
      val = y ** vals[i]
    elif i < 8:
      val = y ** vals[i]
    elif i < 10:
      val = z ** vals[i]
    else:
      val = z ** vals[i]

    if val > max_val:
      max_val = val
      max_index = i

print(results[max_index])