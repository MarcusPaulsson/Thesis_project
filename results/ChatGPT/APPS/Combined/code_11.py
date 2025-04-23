def max_chocolates(n, a, b, p, q):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    count_a = n // a
    count_b = n // b
    lcm_ab = a * (b // gcd(a, b))
    count_ab = n // lcm_ab

    # Calculate chocolates if we prioritize Red tiles
    chocolates_red_first = (count_a - count_ab) * p + (count_b - count_ab) * q + count_ab * max(p, q)

    return chocolates_red_first

# Read input
n, a, b, p, q = map(int, input().split())
# Calculate and print the result
print(max_chocolates(n, a, b, p, q))