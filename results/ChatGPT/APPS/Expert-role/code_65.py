def min_skip_points(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        skip_points = 0
        i = 0
        
        while i < n:
            if a[i] == 1:  # If it's a hard boss
                skip_points += 1  # Use a skip point
                i += 1  # Move to the next boss
            if i < n and a[i] == 0:  # If the next boss is easy
                i += 1  # Kill the easy boss
            if i < n and a[i] == 1:  # If the next boss is hard
                skip_points += 1  # Use another skip point
                i += 1  # Kill the hard boss
            
            # You can skip killing two bosses in one session if both are easy
            if i < n and a[i] == 0:  # If the next boss is easy again
                i += 1  # Kill the easy boss
            
        results.append(skip_points)
        
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = min_skip_points(t, test_cases)

# Print results
for result in results:
    print(result)