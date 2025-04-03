def seat_kids(t, cases):
    results = []
    for n in cases:
        # We can use even numbers from 2n to 4n with step 2
        chairs = list(range(2, 2 * n + 1, 2))
        results.append(chairs)
    return results

# Input handling
t = int(input())
cases = [int(input()) for _ in range(t)]

# Get the results
results = seat_kids(t, cases)

# Print results
for result in results:
    print(" ".join(map(str, result)))