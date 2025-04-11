def has_palindrome_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        # Use a dictionary to track the last index of each number
        last_index = {}
        for i in range(n):
            if a[i] in last_index:
                # If we find the same number again and there's at least one element in between
                if i - last_index[a[i]] > 1:
                    found = True
                    break
            last_index[a[i]] = i
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
results = has_palindrome_subsequence(test_cases)

# Print results
for result in results:
    print(result)