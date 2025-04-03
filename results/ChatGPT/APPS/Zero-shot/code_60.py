def smallest_xor_sum(t, test_cases):
    results = []
    for a, b in test_cases:
        results.append((a ^ b) + (a & b))
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Calculate results
results = smallest_xor_sum(t, test_cases)

# Print output
for result in results:
    print(result)