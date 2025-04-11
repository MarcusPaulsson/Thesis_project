def count_cyclic_strings(n, s):
    from itertools import product

    def is_cyclic_shift(s1, s2):
        return len(s1) == len(s2) and s1 in (s2 + s2)

    # Generate all binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Filter strings that contain s as a substring
    valid_strings = [t for t in all_strings if s in t]
    
    # Use a set to store unique cyclic strings
    unique_cyclic_strings = set()
    
    for t in valid_strings:
        # Generate all cyclic shifts of t
        for i in range(n):
            cyclic_shift = t[i:] + t[:i]
            unique_cyclic_strings.add(cyclic_shift)
    
    return len(unique_cyclic_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))