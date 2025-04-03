def can_reduce_to_one(t, test_cases):
    results = []
    for n, a in test_cases:
        # Find the first index where a[i] < a[i + 1]
        possible = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                possible = True
                break
        results.append("YES" if possible else "NO")
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = can_reduce_to_one(t, test_cases)

# Print results
print("\n".join(results))