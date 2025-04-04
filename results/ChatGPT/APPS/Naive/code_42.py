def count_circular_strings(n, s):
    from itertools import product
    
    # Function to check if s is a substring of any cyclic rotation of t
    def contains_substring(t):
        doubled_t = t + t
        return s in doubled_t
    
    # Generate all possible binary strings of length n
    count = 0
    for t in product('01', repeat=n):
        t_str = ''.join(t)
        if contains_substring(t_str):
            count += 1
            
    return count

# Input
n = int(input().strip())
s = input().strip()

# Output
print(count_circular_strings(n, s))