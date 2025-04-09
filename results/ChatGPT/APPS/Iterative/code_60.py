def has_palindrome_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        last_seen = {}
        for i in range(n):
            if a[i] in last_seen:
                if i - last_seen[a[i]] >= 2:
                    found = True
                    break
            last_seen[a[i]] = i
        results.append("YES" if found else "NO")
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Processing and printing results
results = has_palindrome_subsequence(test_cases)
print("\n".join(results))