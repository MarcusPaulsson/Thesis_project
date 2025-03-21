def max_difference(t, test_cases):
    results = []
    for i in range(t):
        n, k = test_cases[i][0]
        a = test_cases[i][1]
        
        # Find the maximum and minimum amount of water in the barrels
        max_water = max(a)
        min_water = min(a)
        
        # Calculate the maximum possible difference
        total_water = sum(a)
        max_possible = max_water + total_water
        
        # The minimum possible remains the same
        min_possible = min_water
        
        # The result is the difference
        results.append(max_possible - min_possible)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append(((n, k), a))

# Get results and print
results = max_difference(t, test_cases)
for result in results:
    print(result)