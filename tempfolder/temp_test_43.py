def min_time_for_dishes(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]
        
        # Calculate the minimum time
        total_pickup_time = sum(b)
        min_time = float('inf')
        
        for j in range(n):
            # If we take the courier from restaurant j
            delivery_time = a[j]
            # Total time is max of delivery time and the time taken for pickups (excluding b[j])
            current_time = max(delivery_time, total_pickup_time - b[j])
            min_time = min(min_time, current_time)
        
        results.append(min_time)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    b = list(map(int, data[index + 2].split()))
    test_cases.append((n, a, b))
    index += 3

# Get results
results = min_time_for_dishes(t, test_cases)

# Output results
for result in results:
    print(result)