def has_palindrome_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        # Check for any element that appears at least twice with at least one element between them
        first_occurrence = {}
        for i in range(n):
            if a[i] in first_occurrence:
                # If we've seen this element before and it's not adjacent, we found a palindrome
                if i - first_occurrence[a[i]] > 1:
                    found = True
                    break
            # Record the first occurrence of the element
            first_occurrence[a[i]] = i
        
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