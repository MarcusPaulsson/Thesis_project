x = float(input().strip())

# Iterate through all possible pairs (a, b) in the range [1, 10]
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 1e-6:  # Check if the product is close to x
            print(a, b)
            exit()  # Exit after finding the first valid pair