def minimize_max_difference(test_cases):
    results = []
    
    for n, a in test_cases:
        min_val = float('inf')
        max_val = float('-inf')
        
        # Find the minimum and maximum values from non-missing elements
        for value in a:
            if value != -1:
                min_val = min(min_val, value)
                max_val = max(max_val, value)

        # The minimum possible value of m
        m = max(max_val - min_val, 0)
        
        # Choosing k as the average of min_val and max_val
        if min_val == float('inf') or max_val == float('-inf'):
            k = 0
        else:
            k = (min_val + max_val) // 2
        
        results.append((m, k))
    
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = minimize_max_difference(test_cases)
for m, k in results:
    print(m, k)