def has_palindrome_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        # Check for any element that appears at least twice
        indices = {}
        for i in range(n):
            if a[i] in indices:
                # If we find the same element again and the distance is at least 2
                if i - indices[a[i]] >= 2:
                    found = True
                    break
            indices[a[i]] = i
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