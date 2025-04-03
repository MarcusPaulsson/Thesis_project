def count_cyclical_strings(n, s):
    from itertools import product

    len_s = len(s)
    total_count = 0
    seen = set()

    # Generate all possible binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)

        # Check if any cyclic shift of t contains s
        if any(s in t[i:] + t[:i] for i in range(n)):
            if t not in seen:
                seen.add(t)
                total_count += 1

    return total_count

# Read input
n = int(input().strip())
s = input().strip()

# Get the result and print
result = count_cyclical_strings(n, s)
print(result)