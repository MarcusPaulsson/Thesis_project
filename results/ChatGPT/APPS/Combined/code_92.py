x = float(input().strip())

# Calculate integers a and b based on the input x
a = min(max(int(x * 10), 1), 10)
b = min(max(int(x * 10) % 10 + 1, 1), 10)

print(a, b)