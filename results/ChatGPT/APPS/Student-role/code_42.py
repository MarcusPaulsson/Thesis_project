def count_cyclic_strings(n, s):
    from itertools import product

    def is_valid_cyclic(t):
        # Check if s is a substring in any cyclic shift of t
        doubled_t = t + t
        return s in doubled_t

    # Generate all binary strings of length n
    all_binary_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Count valid cyclic strings
    valid_count = sum(1 for t in all_binary_strings if is_valid_cyclic(t))
    
    return valid_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))