def count_good_substrings(s):
    n = len(s)
    good_count = 0
    
    for l in range(n):
        num = 0
        for r in range(l, n):
            # Build the number in decimal from binary
            num = (num << 1) | (1 if s[r] == '1' else 0)
            length = r - l + 1
            if length == num:
                good_count += 1
    
    return good_count

t = int(input())
results = []
for _ in range(t):
    s = input().strip()
    results.append(count_good_substrings(s))

print('\n'.join(map(str, results)))