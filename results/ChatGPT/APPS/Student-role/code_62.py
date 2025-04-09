def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triple = (0, 0, 0)

        for A in range(1, a + 1):
            for k in range(1, 10001):
                B = A * k
                if B < b:
                    continue
                if B > c:
                    break

                C = B * (B // A)
                if C < c:
                    continue

                ops = abs(A - a) + abs(B - b) + abs(C - c)
                if ops < min_ops:
                    min_ops = ops
                    best_triple = (A, B, C)

        results.append((min_ops, best_triple))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Getting results
results = min_operations(t, test_cases)

# Output results
for ops, (A, B, C) in results:
    print(ops)
    print(A, B, C)