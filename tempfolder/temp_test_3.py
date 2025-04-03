def max_difference(t, test_cases):
    results = []
    for n, k, a in test_cases:
        # Calculate the total amount of water in all barrels
        total_water = sum(a)
        # The maximum possible amount in one barrel after pouring k times
        max_possible = total_water
        # The minimum possible amount in one barrel (can be 0 if we pour all water into one barrel)
        min_possible = 0
        # Calculate the maximum difference
        max_diff = max_possible - min_possible
        results.append(max_diff)
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