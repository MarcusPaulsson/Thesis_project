def min_jars_to_empty(test_cases):
    results = []
    for n, jars in test_cases:
        count_1 = jars.count(1)
        count_2 = jars.count(2)
        
        # Calculate the difference
        diff = abs(count_1 - count_2)
        
        # The minimum number of jars to empty
        results.append(diff if diff % 2 == 0 else diff + 2)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    jars = list(map(int, input().split()))
    test_cases.append((n, jars))

# Get results
results = min_jars_to_empty(test_cases)

# Print results
for result in results:
    print(result)