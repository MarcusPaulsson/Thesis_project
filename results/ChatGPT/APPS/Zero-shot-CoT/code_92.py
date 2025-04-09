x = float(input().strip())

# We will find two integers a and b between 1 and 10 such that a * b is close to x
# Since x is between 0 and 5, we can find such integers easily.

found = False
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 0.000001:  # Check if the product is close enough to x
            print(a, b)
            found = True
            break
    if found:
        break