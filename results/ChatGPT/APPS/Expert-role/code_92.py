x = float(input().strip())

# Calculate the integers a and b
a = int(x * 10) % 10 + 1
b = int(x * 10) // 10 + 1

# Ensure a and b are within the range [1, 10]
if a < 1:
    a = 1
if a > 10:
    a = 10
if b < 1:
    b = 1
if b > 10:
    b = 10

print(a, b)