x = float(input().strip())

# Calculate integers a and b such that 1 <= a, b <= 10
# We can use a simple approach to find a and b
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 1e-6:
            print(a, b)
            break