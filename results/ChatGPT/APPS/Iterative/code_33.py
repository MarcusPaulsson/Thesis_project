def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    def generate_ap(a, b, start, end):
        if a == 0:
            return [b] if start <= b <= end else []
        
        if a > 0:
            first = (start - b + a - 1) // a
            last = (end - b) // a
        else:
            first = (end - b) // a
            last = (start - b + a - 1) // a

        first_value = a * first + b
        last_value = a * last + b
        
        if first_value > end or last_value < start:
            return []
        return list(range(first_value, last_value + a, a))

    d = b2 - b1
    a = a1
    b = -a2

    g = gcd(a, -b)
    if d % g != 0:
        print(0)
        return

    a //= g
    b //= g
    d //= g

    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    g, x0, y0 = extended_gcd(a, b)
    x0 *= d
    y0 *= d

    k_min = (L - b1) // a1
    k_max = (R - b1) // a1

    t_min = (x0 - k_max * b) // a if b != 0 else (x0 // a)
    t_max = (x0 - k_min * b) // a if b != 0 else (x0 // a)

    t_start = (t_min + (b - 1)) // b if b > 0 else (t_min // b)
    t_end = t_max // b

    count = max(0, t_end - t_start + 1)
    print(count)

# Example input
count_common_integers(2, 0, 3, 3, 5, 21)
count_common_integers(2, 4, 3, 0, 6, 17)