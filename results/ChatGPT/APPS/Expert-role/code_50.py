def min_jars_to_empty(t, test_cases):
    results = []
    for n, jars in test_cases:
        count_strawberry = jars.count(1)
        count_blueberry = jars.count(2)
        
        # Calculate the difference
        diff = abs(count_strawberry - count_blueberry)
        
        # The number of jars to empty to equalize
        jars_to_empty = diff // 2
        
        # Total jars that would be left
        total_jars_left = n - jars_to_empty
        
        # Minimum jars to eat to achieve equal count
        results.append(total_jars_left * 2)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    jars = list(map(int, input().split()))
    test_cases.append((n, jars))

# Get results
results = min_jars_to_empty(t, test_cases)

# Output results
for result in results:
    print(result)