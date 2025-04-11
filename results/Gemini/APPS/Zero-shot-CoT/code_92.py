x = float(input())
a = int(x * 10)
b = int((x * 10) % 1 * 10)
if b == 0:
    b = 1
print(a, b)