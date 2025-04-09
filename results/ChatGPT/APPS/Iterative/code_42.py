def count_cyclic_strings(n, s):
    from itertools import product

    def is_cyclic(s1, s2):
        return s1 in (s2 + s2)

    # Generate all binary strings of length n
    binary_strings = [''.join(p) for p in product("01", repeat=n)]
    
    # Use a set to track unique cyclical strings that contain s
    unique_cyclic_strings = set()

    # Check each binary string if it contains s in any cyclic shift
    for t in binary_strings:
        if any(is_cyclic(s, t[i:] + t[:i]) for i in range(n)):
            unique_cyclic_strings.add(t)

    return len(unique_cyclic_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))