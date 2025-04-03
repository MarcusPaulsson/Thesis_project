def seat_kids(test_cases):
    results = []
    for n in test_cases:
        # Select even numbers from the range 1 to 4n
        chairs = [i for i in range(2, 4*n + 1, 2)]
        results.append(chairs[:n])
    return results

# Input reading
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Get results
results = seat_kids(test_cases)

# Output results
for res in results:
    print(" ".join(map(str, res)))