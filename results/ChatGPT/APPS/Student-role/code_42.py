def count_cyclic_strings(n, s):
    from itertools import product

    def is_cyclic_shift(s1, s2):
        return len(s1) == len(s2) and s1 in s2 + s2

    # Generate all binary strings of length n
    binary_strings = [''.join(p) for p in product('01', repeat=n)]
    
    distinct_cyclic_strings = set()
    
    for t in binary_strings:
        if s in t:
            # Check for cyclic shifts and add only the canonical form
            min_shift = min(t[i:] + t[:i] for i in range(n))
            distinct_cyclic_strings.add(min_shift)
    
    return len(distinct_cyclic_strings)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))