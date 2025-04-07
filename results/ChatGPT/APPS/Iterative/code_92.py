x = float(input().strip())

# Scale x to the range of 1 to 10
scaled_x = x * 2

# Choose integers a and b such that a / b is close to scaled_x
a = int(scaled_x)
b = 1

# Adjust a and b to ensure they are within the range of 1 to 10
if a < 1:
    a = 1
elif a > 10:
    a = 10

# Since b is initialized to 1, we only adjust it if a is too small
if scaled_x > 10:
    b = 10
else:
    # Select a suitable b to get closer to scaled_x
    b = max(1, min(10, round(a / scaled_x)))

print(a, b)