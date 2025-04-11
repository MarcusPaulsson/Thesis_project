def count_common_ap(a1, b1, a2, b2, L, R):
    def find_first_valid(start, step, limit):
        if step == 0:
            return start if start <= limit else None
        if start > limit:
            return None
        return start + ((limit - start) // step) * step

    def find_last_valid(start, step, limit):
        if step == 0:
            return start if start >= limit else None
        if start < limit:
            return None
        return start - ((start - limit) // step) * step

    # Calculate the first and last valid x in the range [L, R]
    first_x = find_first_valid(b1, a1, R)
    last_x = find_last_valid(b2, a2, L)

    if first_x is None or last_x is None or first_x > last_x:
        return 0

    # Now we need to find the common values in the arithmetic sequences
    # We can express the common values as:
    # x = a1 * k' + b1 = a2 * l' + b2
    # Rearranging gives us:
    # a1 * k' - a2 * l' = b2 - b1
    # This is a linear Diophantine equation.

    d = b2 - b1
    step = a2 // gcd(a1, a2)

    # Find the first valid k' for the equation
    k_start = (d + a2 - 1) // a2 if d > 0 else d // a2
    k_end = (R - b1) // a1

    if k_start > k_end:
        return 0

    # Count the number of valid k'
    count = (k_end - k_start) // step + 1
    return count

def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_ap(a1, b1, a2, b2, L, R)
print(result)