def has_palindrome_subsequence(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        # Check for any element that appears at least twice with at least one element between them
        indices = {}
        for i in range(n):
            if a[i] in indices:
                if i - indices[a[i]] >= 2:
                    found = True
                    break
            indices[a[i]] = i
        results.append("YES" if found else "NO")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = has_palindrome_subsequence(test_cases)
print("\n".join(results))