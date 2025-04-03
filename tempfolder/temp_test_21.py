def find_k(t, test_cases):
    results = []
    for case in test_cases:
        n, S = case
        S_set = set(S)
        found_k = False
        min_k = float('inf')

        for k in range(1, 1024):
            transformed_set = {s ^ k for s in S}
            if transformed_set == S_set:
                found_k = True
                min_k = min(min_k, k)

        results.append(min_k if found_k else -1)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    test_cases.append((n, S))

# Get results
results = find_k(t, test_cases)

# Print results
for result in results:
    print(result)