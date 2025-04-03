x = float(input().strip())

# Calculate the first integer a (1 to 10)
a = int(x) + 1

# Calculate the second integer b (1 to 10)
b = round((x - a) * 10) % 10 + 1

# Adjust if b is 0
if b == 0:
    b = 1

print(a, b)