def min_delivery_time(t, cases):
    results = []
    for n, a, b in cases:
        courier_time = max(a[i] for i in range(n))  # Maximum courier delivery time
        pickup_time = sum(b)  # Total time if Petya picks up all dishes
        min_time = min(courier_time, pickup_time)
        
        # Calculate the minimum time considering both delivery and pickup
        for i in range(n):
            # If Petya picks up dish i, he must account for time spent to get other dishes
            time_with_pickup = sum(b[j] for j in range(n) if j != i)
            min_time = min(min_time, max(a[i], time_with_pickup))
        
        results.append(min_time)
    
    return results

# Read input
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cases.append((n, a, b))

# Get results and print output
results = min_delivery_time(t, cases)
for result in results:
    print(result)