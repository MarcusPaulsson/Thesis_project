x = float(input().strip())

# Using a simple nested loop to find any valid pair (a, b)
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 1e-6:  # Check if the product is approximately equal to x
            print(a, b)
            break
    else:
        continue
    break