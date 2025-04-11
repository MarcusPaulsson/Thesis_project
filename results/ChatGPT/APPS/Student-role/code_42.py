def count_cyclic_strings(n, s):
    from itertools import product

    def is_valid(t):
        # Check if s is a substring of any cyclic shift of t
        double_t = t + t
        return s in double_t

    count = 0
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        if is_valid(t):
            count += 1

    return count

n = int(input().strip())
s = input().strip()
print(count_cyclic_strings(n, s))