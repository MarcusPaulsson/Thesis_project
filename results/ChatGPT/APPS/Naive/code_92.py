x = float(input().strip())

# Calculate the integers a and b based on the input x
a = int(x) + 1
b = int((x - int(x)) * 10) + 1

# Ensure a and b are within the range of 1 to 10
a = min(max(a, 1), 10)
b = min(max(b, 1), 10)

print(a, b)