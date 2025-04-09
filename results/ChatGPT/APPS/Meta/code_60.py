def has_palindromic_subsequence(t, test_cases):
    results = []
    
    for n, a in test_cases:
        found = False
        # Check for any repeated element that is at least 2 indices apart
        seen = {}
        for i in range(n):
            if a[i] in seen:
                if i - seen[a[i]] >= 2:
                    found = True
                    break
            seen[a[i]] = i
        
        if found:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = has_palindromic_subsequence(t, test_cases)

# Output results
for result in results:
    print(result)