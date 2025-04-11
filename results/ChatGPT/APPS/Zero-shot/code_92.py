x = float(input().strip())

# We will iterate through possible values for a and b
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a ** 2 + b ** 2 - x) < 1e-6:
            print(a, b)
            break