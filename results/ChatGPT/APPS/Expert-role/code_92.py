x = float(input().strip())

# We need to find two integers a and b such that 1 <= a, b <= 10
# and a * b is approximately equal to x

# We can iterate through possible values of a and b
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 1e-6:  # Check if the product is close to x
            print(a, b)
            break