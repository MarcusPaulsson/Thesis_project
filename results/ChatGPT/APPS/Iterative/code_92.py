x = float(input().strip())

# We will find two integers a and b such that 1 <= a, b <= 10 and a * b / (a + b) = x
# This is equivalent to finding integers a and b such that a * b = x * (a + b)

for a in range(1, 11):
    for b in range(1, 11):
        if abs(a * b / (a + b) - x) < 1e-6:
            print(a, b)
            exit()  # Use exit to stop the program after finding the first solution