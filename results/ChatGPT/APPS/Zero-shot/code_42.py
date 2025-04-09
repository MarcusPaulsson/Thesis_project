def count_cyclic_strings(n, s):
    from itertools import product
    
    m = len(s)
    
    # Generate all binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Count distinct cyclic strings that contain s
    distinct_cyclic_strings = set()
    
    for t in all_strings:
        # Check if s is a substring of any cyclic shift of t
        cyclic = t + t  # Concatenate to simulate cyclic shifts
        if s in cyclic:
            distinct_cyclic_strings.add(t)
    
    return len(distinct_cyclic_strings)

# Read input
n = int(input())
s = input().strip()

# Calculate and print the result
result = count_cyclic_strings(n, s)
print(result)