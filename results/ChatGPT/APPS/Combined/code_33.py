def count_common_ap(a1, b1, a2, b2, L, R):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def find_first_valid(start, step, offset):
        if step == 0:
            return offset if start <= offset <= R else None
        if start > R:
            return None
        if start < L:
            if (L - offset) % step == 0:
                return L
            return L + (step - (L - offset) % step) % step
        return start + (step - (start - offset) % step) % step

    def find_last_valid(end, step, offset):
        if step == 0:
            return offset if L <= offset <= end else None
        if end < L:
            return None
        if end > R:
            if (R - offset) % step == 0:
                return R
            return R - (R - offset) % step
        return end - (end - offset) % step

    step = a1 * a2 // gcd(a1, a2)
    offset = b2 - b1

    first_x = find_first_valid(L, step, b1)
    last_x = find_last_valid(R, step, b1)

    if first_x is None or last_x is None or first_x > last_x:
        return 0

    return (last_x - first_x) // step + 1

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_ap(a1, b1, a2, b2, L, R))