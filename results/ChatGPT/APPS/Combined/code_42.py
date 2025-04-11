def count_cyclic_strings(n, s):
    from itertools import product

    # Function to check if a string contains s as a substring
    def contains_substring(t, s):
        return s in t

    # Generate all binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    distinct_cyclic_strings = set()

    for t in all_strings:
        # Check all cyclic shifts of t
        for i in range(n):
            cyclic_shift = t[i:] + t[:i]
            if contains_substring(cyclic_shift, s):
                distinct_cyclic_strings.add(t)
                break  # No need to check further shifts for this string

    return len(distinct_cyclic_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))