def can_reduce_to_one(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                found = True
                break
        results.append("YES" if found else "NO")
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Getting results
results = can_reduce_to_one(test_cases)

# Printing results
print("\n".join(results))