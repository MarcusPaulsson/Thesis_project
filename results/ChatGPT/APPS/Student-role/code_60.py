def has_palindrome_subsequence(test_cases):
    results = []
    for a in test_cases:
        n = len(a)
        found = False
        # Using a set to track the indices of each number
        indices = {}
        for i in range(n):
            if a[i] in indices:
                # If we have seen this number before, we can form a palindrome
                # Check the distance from the last occurrence
                if i - indices[a[i]] > 1:
                    found = True
                    break
            # Update the last occurrence index
            indices[a[i]] = i
        results.append("YES" if found else "NO")
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append(a)

# Get results
results = has_palindrome_subsequence(test_cases)

# Output results
for result in results:
    print(result)