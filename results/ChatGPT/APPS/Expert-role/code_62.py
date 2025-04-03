def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        # Initialize minimum operations and best triple
        min_ops = float('inf')
        best_triple = (0, 0, 0)

        # Iterate over possible values for A
        for A in range(1, a + 1):
            # B must be a multiple of A, find suitable B
            for B in range(A, c + 1, A):
                # C must be a multiple of B, find suitable C
                for C in range(B, c + 1, B):
                    # Calculate operations needed
                    ops = abs(A - a) + abs(B - b) + abs(C - c)
                    if ops < min_ops:
                        min_ops = ops
                        best_triple = (A, B, C)

        results.append((min_ops, best_triple))

    return results

# Input reading
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for res in results:
    print(res[0])
    print(*res[1])