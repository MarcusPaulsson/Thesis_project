def count_cyclic_strings(n, s):
    from itertools import product
    
    len_s = len(s)
    count = 0
    seen = set()
    
    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        
        # Check if s is a substring in any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            # Normalize t to account for cyclic shifts
            min_rotation = min(t[i:] + t[:i] for i in range(n))
            if min_rotation not in seen:
                seen.add(min_rotation)
                count += 1

    return count

# Input reading
n = int(input().strip())
s = input().strip()

# Function call and output
print(count_cyclic_strings(n, s))