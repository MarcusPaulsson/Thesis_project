x = float(input().strip())

# We need to find integers a and b such that 1 <= a, b <= 10 and a * b is approximately equal to x
# The simplest approach is to iterate through all possible values for a and b
for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b - x) < 1e-6:  # Use a small tolerance for floating point comparison
            print(a, b)
            break