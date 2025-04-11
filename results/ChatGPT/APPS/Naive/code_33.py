def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the initial offsets
    step = gcd(a1, a2)
    
    # Normalize the offsets
    b1_mod = (b1 % step + step) % step
    b2_mod = (b2 % step + step) % step

    # Check if the offsets are compatible
    if b1_mod != b2_mod:
        return 0

    # Find the first valid x >= L
    first_x = max(L, (b1 + (L - b1) // a1 * a1))
    if (first_x - b1) % a1 != 0:
        first_x += a1

    # Find the last valid x <= R
    last_x = min(R, (b1 + (R - b1) // a1 * a1))
    if (last_x - b1) % a1 != 0:
        last_x -= a1

    # Count the number of valid integers
    if first_x > last_x:
        return 0

    return (last_x - first_x) // step + 1

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())

# Get the result and print it
result = count_common_integers(a1, b1, a2, b2, L, R)
print(result)