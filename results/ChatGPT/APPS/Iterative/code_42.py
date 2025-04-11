def count_cyclic_strings(n, s):
    from itertools import product

    len_s = len(s)
    total_count = 0
    seen = set()

    # Generate all binary strings of length n
    for t in product('01', repeat=n):
        t = ''.join(t)
        # Check if s is a substring of any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            # Store the canonical form of the cyclic string to avoid duplicates
            min_rotation = min(t[i:] + t[:i] for i in range(n))
            seen.add(min_rotation)

    return len(seen)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))