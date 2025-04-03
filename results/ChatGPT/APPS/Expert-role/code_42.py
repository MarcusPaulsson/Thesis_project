def count_cyclic_strings(n, s):
    from itertools import product
    
    m = len(s)
    count = 0
    seen = set()
    
    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check for all cyclic shifts of t
        for i in range(n):
            if s in t[i:] + t[:i]:
                # If we found a cyclic shift containing s, add to seen
                seen.add(t)
                break

    return len(seen)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))