def count_cyclical_strings(n, s):
    from itertools import product

    def is_valid(t):
        # Check if s is a substring of any cyclic shift of t
        double_t = t + t
        return s in double_t

    count = 0
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        if is_valid(t):
            count += 1

    return count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_cyclical_strings(n, s))