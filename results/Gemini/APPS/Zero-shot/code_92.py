x = float(input())

a = int((x * 10) // 1)
b = int((x * 10) % 1 * 10 + 1)
if b > 10:
  b = 10
if a == 0:
  a = 1

print(a, b)