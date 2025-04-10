def count_cyclic_binary_strings(n, s):
    from itertools import product

    total_count = 0
    seen = set()

    # Generate all possible binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if any cyclic shift of t contains s as a substring
        if any(s in t[i:] + t[:i] for i in range(n)):
            seen.add(t)

    return len(seen)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_binary_strings(n, s))