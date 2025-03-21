def find_minimum_k(test_cases):
    results = []
    
    for s in test_cases:
        S = set(s)
        found = False
        min_k = float('inf')

        for x in S:
            k = x ^ 0  # This is essentially just x, since k must be > 0.
            new_set = {y ^ k for y in S}
            if new_set == S and k > 0:
                found = True
                min_k = min(min_k, k)

        if found:
            results.append(min_k)
        else:
            results.append(-1)

    return results


# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    test_cases.append(s)

# Get results
results = find_minimum_k(test_cases)

# Print results
for result in results:
    print(result)