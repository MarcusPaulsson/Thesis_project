x = float(input().strip())

# Calculate the integers a and b
a = 1
b = int(round(x * 10 / a))

# Ensure b is within the range [1, 10]
while b < 1 or b > 10:
    a += 1
    b = int(round(x * 10 / a))

print(a, b)