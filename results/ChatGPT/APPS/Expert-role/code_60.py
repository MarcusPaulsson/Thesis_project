def has_palindrome_subsequence(t, test_cases):
    results = []
    for n, a in test_cases:
        found = False
        index_map = {}
        for i in range(n):
            if a[i] in index_map:
                if i - index_map[a[i]] >= 2:
                    found = True
                    break
            index_map[a[i]] = i
        results.append("YES" if found else "NO")
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = has_palindrome_subsequence(t, test_cases)

# Print results
for result in results:
    print(result)