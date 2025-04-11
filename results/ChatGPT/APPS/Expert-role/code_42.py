def count_cyclic_strings(n, s):
    from itertools import product

    def is_cyclic_shift(s1, s2):
        return len(s1) == len(s2) and s1 in (s2 + s2)

    def contains_substring(cyclic_str, substring):
        for i in range(len(cyclic_str)):
            if substring in cyclic_str[i:] + cyclic_str[:i]:
                return True
        return False

    distinct_strings = set()
    for bits in product('01', repeat=n):
        t = ''.join(bits)
        if contains_substring(t, s):
            distinct_strings.add(t)

    return len(distinct_strings)

n = int(input())
s = input().strip()
result = count_cyclic_strings(n, s)
print(result)