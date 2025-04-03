def seat_kids(t, test_cases):
    results = []
    for n in test_cases:
        # Select the even numbers from 1 to 4n
        chairs = [i for i in range(1, 4 * n + 1) if i % 2 == 0]
        results.append(chairs[:n])
    return results

# Read input
t = int(input().strip())
test_cases = [int(input().strip()) for _ in range(t)]

# Get results
results = seat_kids(t, test_cases)

# Print results
for res in results:
    print(' '.join(map(str, res)))