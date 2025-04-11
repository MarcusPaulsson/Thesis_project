x = float(input().strip())

# Scale x to a range suitable for generating integers between 1 and 10
scaled_x = x * 10

# Generate two integers based on the scaled value
a = int(scaled_x) % 10 + 1
b = (int(scaled_x * 2) % 10) + 1

print(a, b)