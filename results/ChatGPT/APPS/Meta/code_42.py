def count_cyclic_strings(n, s):
    from itertools import product

    # Generate all possible binary strings of length n
    all_strings = [''.join(p) for p in product('01', repeat=n)]
    
    # Function to check if s is a substring of any cyclic shift of t
    def contains_as_substring(t, s):
        double_t = t + t  # Concatenate t with itself to check cyclic shifts
        return s in double_t

    # Count distinct cyclic strings that contain s as a substring
    count = 0
    seen = set()
    
    for t in all_strings:
        if contains_as_substring(t, s):
            # Normalize the cyclic string to avoid counting shifts as different
            min_rotation = min(t[i:] + t[:i] for i in range(n))
            if min_rotation not in seen:
                seen.add(min_rotation)
                count += 1

    return count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))