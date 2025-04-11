x = float(input().strip())

# We need to find two integers a and b such that 1 <= a, b <= 10
# and a * b is approximately equal to x

# Initialize the output variables
a, b = 1, 1

# Iterate through possible values for a and b
for i in range(1, 11):
    for j in range(1, 11):
        if abs(i * j - x) < 1e-6:  # Check if the product is close to x
            a, b = i, j
            break
    else:
        continue
    break

print(a, b)