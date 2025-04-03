def minimum_time_to_home(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]
        
        # Calculate the minimum time
        min_time = float('inf')
        total_pickup_time = 0
        
        for j in range(n):
            total_pickup_time += b[j]
            min_time = min(min_time, max(total_pickup_time, a[j]))
        
        results.append(min_time)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Get results
results = minimum_time_to_home(t, test_cases)

# Output results
for result in results:
    print(result)