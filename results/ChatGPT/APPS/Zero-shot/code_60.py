def has_palindrome_subsequence(t, test_cases):
    results = []
    for n, a in test_cases:
        found = False
        # Use a dictionary to track the last seen index of each number
        last_seen = {}
        for i in range(n):
            if a[i] in last_seen:
                # Check if we have seen this number before
                if i - last_seen[a[i]] >= 2:
                    found = True
                    break
            last_seen[a[i]] = i
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