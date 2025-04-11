def count_cyclic_strings(n, s):
    from itertools import product

    # Function to check if s is a substring in any cyclic shift of t
    def contains_as_substring(t):
        doubled_t = t + t  # Concatenate to check cyclic shifts
        return s in doubled_t

    # Generate all binary strings of length n
    total_count = 0
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        if contains_as_substring(t):
            total_count += 1

    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))