def count_good_substrings(s):
    n = len(s)
    good_count = 0
    
    for l in range(n):
        num = 0
        for r in range(l, n):
            num = num * 2 + (1 if s[r] == '1' else 0)
            if r - l + 1 == num:
                good_count += 1
            if num > r - l + 1:  # No need to continue if num exceeds the length
                break
                
    return good_count

t = int(input())
results = []
for _ in range(t):
    s = input().strip()
    results.append(count_good_substrings(s))

print('\n'.join(map(str, results)))