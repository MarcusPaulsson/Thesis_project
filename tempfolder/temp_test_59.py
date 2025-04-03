def minimize_difference(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        min_value = float('inf')
        max_value = float('-inf')
        
        # Finding the min and max of the known elements
        for value in a:
            if value != -1:
                min_value = min(min_value, value)
                max_value = max(max_value, value)
        
        # The minimum absolute difference can be determined
        # by the maximum of the distances from k to the nearest known values.
        # We can take k as the midpoint to minimize the differences.
        k = (min_value + max_value) // 2
        if (min_value + max_value) % 2 == 1:  # If the sum is odd
            # Two choices can be made, we can take either floor or ceil
            # We'll take the floor here, but we could return both as valid.
            k1 = k
            k2 = k + 1
            
            m1 = max(abs(k1 - min_value), abs(k1 - max_value))
            m2 = max(abs(k2 - min_value), abs(k2 - max_value))
            
            if m1 < m2:
                results.append((m1, k1))
            else:
                results.append((m2, k2))
        else:
            m = max(abs(k - min_value), abs(k - max_value))
            results.append((m, k))
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and output results
results = minimize_difference(t, test_cases)
for m, k in results:
    print(m, k)