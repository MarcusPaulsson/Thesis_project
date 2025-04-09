def count_cyclic_strings(n, s):
    from itertools import product

    m = len(s)
    total_strings = 0
    all_strings = set()

    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if s is a substring of any cyclic shift of t
        if any(s in t[i:] + t[:i] for i in range(n)):
            all_strings.add(t)

    total_strings = len(all_strings)
    return total_strings

# Input handling
n = int(input().strip())
s = input().strip()

# Calculate and print the result
result = count_cyclic_strings(n, s)
print(result)