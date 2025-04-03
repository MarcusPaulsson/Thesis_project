def find_permutation_with_same_fingerprint(t, test_cases):
    results = []
    for n, p in test_cases:
        # A simple way to generate a different permutation is to rotate the original
        p_prime = p[1:] + p[:1]
        results.append(p_prime)
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Get results
results = find_permutation_with_same_fingerprint(t, test_cases)

# Output results
for result in results:
    print(" ".join(map(str, result)))