def max_operations(t, test_cases):
    results = []
    for n, s in test_cases:
        count = 0
        i = 0
        
        while i < n:
            count += 1
            char = s[i]
            while i < n and s[i] == char:
                i += 1
            while i < n and s[i] != char:
                i += 1
        
        results.append(count)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Get results
results = max_operations(t, test_cases)

# Output results
for result in results:
    print(result)