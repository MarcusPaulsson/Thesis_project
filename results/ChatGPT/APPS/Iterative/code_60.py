def has_palindrome_subsequence(t, test_cases):
    results = []
    for n, a in test_cases:
        found = False
        last_occurrence = {}
        for i in range(n):
            if a[i] in last_occurrence:
                # Check if the distance between the same elements is at least 2
                if i - last_occurrence[a[i]] >= 2:
                    found = True
                    break
            last_occurrence[a[i]] = i
        results.append("YES" if found else "NO")
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = has_palindrome_subsequence(t, test_cases)

# Output results
for result in results:
    print(result)