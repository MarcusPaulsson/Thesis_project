def count_cyclic_strings(n, s):
    from itertools import product

    def is_valid(t):
        # Check if s is a substring of any cyclic shift of t
        doubled_t = t + t
        return s in doubled_t

    # Generate all binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Count distinct cyclic strings that contain s as a substring
    count = 0
    seen = set()
    
    for t in all_strings:
        if is_valid(t):
            # To avoid counting cyclic shifts as different strings, we use a canonical form
            min_t = min(t[i:] + t[:i] for i in range(n))
            if min_t not in seen:
                seen.add(min_t)
                count += 1

    return count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))