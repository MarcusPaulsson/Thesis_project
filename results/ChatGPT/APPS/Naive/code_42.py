def count_cyclic_strings(n, s):
    from itertools import product

    # Function to check if s is a substring in any cyclic shift of t
    def contains_as_substring(t, s):
        doubled_t = t + t  # Create a doubled version of t to check cyclic shifts
        return s in doubled_t

    # Generate all possible binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Count distinct cyclic strings containing s as a substring
    distinct_cyclic_strings = set()
    
    for t in all_strings:
        if contains_as_substring(t, s):
            distinct_cyclic_strings.add(t)

    return len(distinct_cyclic_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))