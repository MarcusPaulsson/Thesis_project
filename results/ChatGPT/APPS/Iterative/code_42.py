def count_cyclical_strings(n, s):
    from itertools import product
    
    len_s = len(s)
    all_strings = set()
    
    # Generate all binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if any cyclical shift of t contains s as a substring
        if any(s in t[i:] + t[:i] for i in range(n)):
            all_strings.add(t)

    return len(all_strings)

# Read input
n = int(input().strip())
s = input().strip()

# Ensure the string s is not longer than n
if len(s) > n:
    print(0)
else:
    # Get the result
    result = count_cyclical_strings(n, s)
    # Print the result
    print(result)