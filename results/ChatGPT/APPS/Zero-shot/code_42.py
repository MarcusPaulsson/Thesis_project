def count_cyclic_strings(n, s):
    from itertools import product

    len_s = len(s)
    total_count = 0
    seen = set()

    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if s is a substring of any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            seen.add(t)

    return len(seen)

n = int(input().strip())
s = input().strip()
print(count_cyclic_strings(n, s))