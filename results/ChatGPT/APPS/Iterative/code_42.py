def count_cyclical_strings(n, s):
    from itertools import product

    s_len = len(s)
    total_count = 0
    seen = set()

    # Generate all possible binary strings of length n
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        # Check if any cyclical shift contains the substring s
        if any(s in (t[i:] + t[:i]) for i in range(n)):
            seen.add(t)  # No need to check if it's already seen
            total_count += 1

    return total_count

# Input reading
n = int(input("Enter the length of the binary strings: "))
s = input("Enter the substring to check: ").strip()

# Result calculation and output
result = count_cyclical_strings(n, s)
print(result)