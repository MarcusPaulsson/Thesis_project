def has_palindrome_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        # Create a dictionary to track the last seen index of each number
        last_seen = {}
        for i in range(n):
            if a[i] in last_seen:
                # If we find the same number again, check if the distance is at least 2
                if i - last_seen[a[i]] >= 2:
                    found = True
                    break
            # Update the last seen index of the current number
            last_seen[a[i]] = i
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
results = has_palindrome_subsequence(test_cases)

# Output results
for result in results:
    print(result)