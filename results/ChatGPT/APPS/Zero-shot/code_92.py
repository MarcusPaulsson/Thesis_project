def count_cyclical_strings(n, s):
    from itertools import product

    m = len(s)
    total_count = 0
    seen = set()

    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check for all cyclical shifts
        for i in range(n):
            if s in t[i:] + t[:i]:  # Check if s is a substring in this shift
                seen.add(t)
                break

    return len(seen)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclical_strings(n, s))