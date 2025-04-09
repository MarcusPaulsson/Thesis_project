x = float(input().strip())

# To find two integers a and b such that 1 <= a, b <= 10 and a/b = x
# We will iterate through all possible pairs of (a, b)
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a / b - x) < 1e-6:  # Check if the division is approximately equal to x
            print(a, b)
            break
    else:
        continue
    break