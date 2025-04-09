def count_cyclic_strings(n, s):
    from itertools import product

    # Length of the substring to find
    len_s = len(s)
    
    # All possible binary strings of length n
    all_strings = set(''.join(p) for p in product('01', repeat=n))
    
    # Filter to find cyclic strings that contain s as a substring
    valid_cyclic_strings = set()
    
    for t in all_strings:
        # Check all cyclic shifts of t
        cyclic_shifts = [t[i:] + t[:i] for i in range(n)]
        for shift in cyclic_shifts:
            if s in shift:
                valid_cyclic_strings.add(t)
                break
                
    return len(valid_cyclic_strings)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_cyclic_strings(n, s))