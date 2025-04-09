def count_cyclic_strings(n, s):
    from itertools import product
    
    len_s = len(s)
    total_count = 0
    seen_strings = set()
    
    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        
        # Check if s is a substring of any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            seen_strings.add(t)

    return len(seen_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))