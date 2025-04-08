def minimum_operations(test_cases):
    results = []

    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triple = (a, b, c)

        # Try all valid values of A, B, C
        for A in range(1, a + 2):  # A can be from 1 to a + 1
            for B in range(max(A, b - 1), b + 2):  # B must be >= A
                if B % A == 0:  # Check if B is divisible by A
                    for C in range(max(B, c - 1), c + 2):  # C must be >= B
                        if C % B == 0:  # Check if C is divisible by B
                            operations = abs(A - a) + abs(B - b) + abs(C - c)
                            if operations < min_operations:
                                min_operations = operations
                                best_triple = (A, B, C)

        results.append((min_operations, best_triple))

    return results


# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = minimum_operations(test_cases)

# Print output
for res in results:
    print(res[0])
    print(*res[1])