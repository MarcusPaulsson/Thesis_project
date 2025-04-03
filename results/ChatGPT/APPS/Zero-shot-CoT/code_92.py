x = float(input().strip())

# Iterate through all pairs of integers (a, b) where 1 <= a, b <= 10
for a in range(1, 11):
    for b in range(1, 11):
        # Check if the condition is satisfied
        if abs(a * b - x) < 1e-6:
            print(a, b)
            break
    else:
        continue
    break