def has_palindrome_subsequence(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        found = False
        index_map = {}
        
        for i in range(n):
            if a[i] in index_map:
                # Check if the same number has appeared before
                if (i - index_map[a[i]]) > 1:
                    found = True
                    break
            index_map[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and print results
results = has_palindrome_subsequence(t, test_cases)
for result in results:
    print(result)