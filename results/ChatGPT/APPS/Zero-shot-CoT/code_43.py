def min_time_to_get_dishes(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a, b = case
        # Initialize minimum time as infinity
        min_time = float('inf')
        
        # Calculate the time for each possible scenario
        for i in range(n):
            # If Petya picks up from restaurant i
            time_if_pick_up = sum(b[j] for j in range(n) if j != i)
            # If using delivery from restaurant i
            time_if_delivery = a[i]
            # The total time is the maximum of both scenarios
            current_time = max(time_if_pick_up, time_if_delivery)
            min_time = min(min_time, current_time)
        
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
results = min_time_to_get_dishes(t, test_cases)

# Output results
for res in results:
    print(res)