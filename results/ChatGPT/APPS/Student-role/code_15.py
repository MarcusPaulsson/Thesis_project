def max_window_area(t, test_cases):
    results = []
    for a, b, x, y in test_cases:
        # Calculate the maximum area avoiding the dead pixel
        max_area = max(x * b, (a - x - 1) * b, a * y, a * (b - y - 1))
        results.append(max_area)
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = max_window_area(t, test_cases)

# Print results
for result in results:
    print(result)