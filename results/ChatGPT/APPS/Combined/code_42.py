def count_distinct_cyclical_strings(n, s):
    from itertools import product

    # Generate all possible binary strings of length n
    all_strings = (''.join(p) for p in product('01', repeat=n))
    
    distinct_cyclical_strings = set()
    
    for t in all_strings:
        # Check if any cyclical shift of t contains s
        if any(s in (t[i:] + t[:i]) for i in range(n)):
            distinct_cyclical_strings.add(t)

    return len(distinct_cyclical_strings)

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_distinct_cyclical_strings(n, s))