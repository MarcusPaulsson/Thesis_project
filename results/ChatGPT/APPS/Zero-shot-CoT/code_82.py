def find_different_permutation(t, test_cases):
    results = []
    for n, p in test_cases:
        # Simple approach: reverse the array
        p_prime = p[::-1]
        # Ensure it's different from p
        if p_prime == p:
            # If the reverse is the same, we can swap the first two elements
            p_prime[0], p_prime[1] = p_prime[1], p_prime[0]
        results.append(p_prime)
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Get results and print them
results = find_different_permutation(t, test_cases)
for res in results:
    print(' '.join(map(str, res)))