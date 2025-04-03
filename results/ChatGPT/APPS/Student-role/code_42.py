def count_good_substrings(s):
    n = len(s)
    count = 0
    
    for l in range(n):
        num = 0
        for r in range(l, n):
            num = num * 2 + int(s[r])
            if r - l + 1 == num:
                count += 1
            # Early stop if num exceeds the length of the substring
            if num > r - l + 1:
                break
    
    return count

t = int(input())
results = []
for _ in range(t):
    s = input().strip()
    results.append(count_good_substrings(s))

print("\n".join(map(str, results)))