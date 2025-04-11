def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triple = (0, 0, 0)

        for A in range(1, a + 1):
            for B in range(A, c + 1):
                if B % A == 0:
                    C = B * (B // A)
                    if C >= B:
                        ops = abs(A - a) + abs(B - b) + abs(C - c)
                        if ops < min_ops:
                            min_ops = ops
                            best_triple = (A, B, C)

        results.append((min_ops, best_triple))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for ops, (A, B, C) in results:
    print(ops)
    print(A, B, C)