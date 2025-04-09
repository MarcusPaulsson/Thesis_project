def has_palindrome_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        seen = {}
        found = False
        for i in range(n):
            if a[i] in seen:
                if i - seen[a[i]] >= 2:
                    found = True
                    break
            seen[a[i]] = i
        results.append("YES" if found else "NO")
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = has_palindrome_subsequence(t, test_cases)
for result in results:
    print(result)