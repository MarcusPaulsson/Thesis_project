def count_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Find the first valid x in the range [L, R]
    def first_valid_x():
        for k in range((L - b1 + a1 - 1) // a1, (R - b1) // a1 + 1):
            x = a1 * k + b1
            if L <= x <= R:
                return x
        return None

    # Find the last valid x in the range [L, R]
    def last_valid_x():
        for k in range((R - b1) // a1, (L - b1 - 1) // a1, -1):
            x = a1 * k + b1
            if L <= x <= R:
                return x
        return None

    # Find the first valid x from the second progression
    def first_valid_x2():
        for l in range((L - b2 + a2 - 1) // a2, (R - b2) // a2 + 1):
            x = a2 * l + b2
            if L <= x <= R:
                return x
        return None

    # Find the last valid x from the second progression
    def last_valid_x2():
        for l in range((R - b2) // a2, (L - b2 - 1) // a2, -1):
            x = a2 * l + b2
            if L <= x <= R:
                return x
        return None

    # Get the first and last valid x from both progressions
    x1 = first_valid_x()
    x2 = first_valid_x2()
    
    if x1 is None and x2 is None:
        return 0

    if x1 is None:
        x1 = x2
    if x2 is None:
        x2 = x1

    # Ensure x1 is the smaller one
    x1, x2 = min(x1, x2), max(x1, x2)

    # Count the number of valid integers in the range [L, R]
    count = 0
    for x in range(x1, x2 + 1, step):
        if L <= x <= R:
            count += 1

    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_integers(a1, b1, a2, b2, L, R)
print(result)