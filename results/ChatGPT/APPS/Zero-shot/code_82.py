def find_different_permutation(t, cases):
    results = []
    for n, p in cases:
        # A simple strategy is to rotate the permutation
        p_prime = p[1:] + p[:1]
        results.append(p_prime)
    return results

# Reading input
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    cases.append((n, p))

# Finding different permutations
results = find_different_permutation(t, cases)

# Outputting results
for result in results:
    print(' '.join(map(str, result)))