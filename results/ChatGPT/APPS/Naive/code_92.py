x = float(input().strip())

# Find two integers a and b such that 1 <= a, b <= 10 and a / b is approximately equal to x
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a / b - x) < 1e-6:
            print(a, b)
            break