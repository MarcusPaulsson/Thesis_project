x = float(input().strip())

# Scale x to a range that fits into integers 1 to 10
# We can use a simple transformation
a = int((x * 10) % 10) + 1
b = int((x * 10) // 10) + 1

# Ensure both are in the range of 1 to 10
if a < 1:
    a = 1
if b < 1:
    b = 1
if a > 10:
    a = 10
if b > 10:
    b = 10

print(a, b)