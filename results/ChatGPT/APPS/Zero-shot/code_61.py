def max_chocolates(n, a, b, p, q):
    count_red = n // a
    count_blue = n // b
    count_both = n // (a * b // math.gcd(a, b))  # Count tiles painted both colors

    # Calculate chocolates if we prioritize Red over Blue
    chocolates_red_first = (count_red - count_both) * p + (count_blue - count_both) * q + count_both * max(p, q)

    return chocolates_red_first

import math
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))