x = float(input())
a = int(x * 2.2)
b = int(x * 2.2)
if a > 10:
  a = 10
if b > 10:
  b = 10
if a < 1:
  a = 1
if b < 1:
  b = 1
print(a, b)