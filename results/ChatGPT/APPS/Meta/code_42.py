def count_circular_binary_strings(n, s):
    from itertools import product

    m = len(s)
    count = 0
    seen = set()

    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if s is a substring in any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            # Add the string in its canonical form to avoid duplicates
            canonical = min(t[i:] + t[:i] for i in range(n))
            seen.add(canonical)

    return len(seen)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_circular_binary_strings(n, s))