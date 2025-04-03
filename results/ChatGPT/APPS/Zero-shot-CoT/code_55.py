def max_equal_sticks(test_cases):
    results = []
    for n in test_cases:
        # The maximum number of sticks of the same length is given by
        # (n + 1) // 2
        results.append((n + 1) // 2)
    return results

# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Get results
results = max_equal_sticks(test_cases)

# Print results
for result in results:
    print(result)