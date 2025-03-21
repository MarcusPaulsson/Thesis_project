def max_water_difference(t, test_cases):
    results = []
    for n, k, a in test_cases:
        if k == 0 or all(x == 0 for x in a):
            results.append(0)
            continue
        
        total_water = sum(a)
        min_water = min(a)
        
        # The maximum possible water in one barrel after k pours
        max_possible = total_water
        
        # The minimum possible water in one barrel after k pours can be calculated
        # Since we can pour from k barrels, we can leave n-k barrels with their original amounts
        # The minimum of those barrels will remain unchanged
        # So the minimum water in a barrel can only be the minimum of the remaining barrels
        # if we have poured out k times.
        
        results.append(max_possible - min_water)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))

# Get results and print them
results = max_water_difference(t, test_cases)
for result in results:
    print(result)