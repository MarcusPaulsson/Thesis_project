x = float(input().strip())

# The formula to determine the integers a and b based on the input x
# is derived from the formula x = (a * b) / (a + b).
# We will search for integers a and b in the range [1, 10].

found = False
for a in range(1, 11):
    for b in range(1, 11):
        if abs(x - (a * b) / (a + b)) < 1e-6:
            print(a, b)
            found = True
            break
    if found:
        break