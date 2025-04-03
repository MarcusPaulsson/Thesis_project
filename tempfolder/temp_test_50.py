def min_jars_to_empty(test_cases):
    results = []
    for n, jars in test_cases:
        count_strawberry = jars.count(1)
        count_blueberry = jars.count(2)
        
        # The difference between the two counts
        diff = abs(count_strawberry - count_blueberry)
        
        # Number of jars to empty to make counts equal
        if diff == 0:
            results.append(0)
        else:
            results.append(diff)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    jars = list(map(int, input().split()))
    test_cases.append((n, jars))

# Get results and print
results = min_jars_to_empty(test_cases)
for result in results:
    print(result)