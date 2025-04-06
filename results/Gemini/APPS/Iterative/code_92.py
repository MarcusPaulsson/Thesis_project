x = float(input())
a = int(x * 10) % 10
b = int(round((x * 100) % 10))
if a == 0:
  a = 10
if b == 0:
  b = 10
print(a, b)