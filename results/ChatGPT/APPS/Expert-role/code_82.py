def find_different_permutation(t, test_cases):
    results = []
    for n, p in test_cases:
        # A simple way to produce a different permutation is to just rotate it
        # one position to the right.
        p_prime = p[-1:] + p[:-1]
        results.append(p_prime)
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Find different permutations
results = find_different_permutation(t, test_cases)

# Print results
for result in results:
    print(' '.join(map(str, result)))