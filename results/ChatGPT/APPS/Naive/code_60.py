def has_palindromic_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        seen = {}
        
        for i in range(n):
            if a[i] in seen:
                if i - seen[a[i]] > 1:  # Check distance between occurrences
                    found = True
                    break
            seen[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = has_palindromic_subsequence(t, test_cases)
print("\n".join(results))