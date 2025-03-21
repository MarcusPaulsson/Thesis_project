def max_difference(t, test_cases):
    results = []
    for case in test_cases:
        n, k = case[0], case[1]
        a = case[2]
        
        # If all barrels are empty, the difference is 0
        if all(amount == 0 for amount in a):
            results.append(0)
            continue
        
        # Sort the array to find the maximum and minimum easily
        a.sort()
        
        # The maximum possible amount after k pours will be the sum of the largest k+1 barrels
        max_water = sum(a[-(k + 1):])
        
        # The minimum possible amount after k pours will be the sum of the smallest barrel
        min_water = a[0]
        
        # Calculate the difference
        results.append(max_water - min_water)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))

# Get results and print them
results = max_difference(t, test_cases)
for result in results:
    print(result)