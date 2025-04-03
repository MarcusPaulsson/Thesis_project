def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triplet = (a, b, c)

        # Iterate over possible values of A
        for A in range(1, a + 1):
            # Calculate possible B values that are multiples of A
            for k in range(1, (c // A) + 2):
                B = A * k
                if B < b:
                    continue

                # Calculate possible C values that are multiples of B
                for m in range(1, (c // B) + 2):
                    C = B * m
                    if C < c:
                        continue

                    # Calculate operations needed
                    ops = abs(A - a) + abs(B - b) + abs(C - c)
                    if ops < min_ops:
                        min_ops = ops
                        best_triplet = (A, B, C)

        results.append((min_ops, best_triplet))

    return results

# Read input data
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Print output
for res in results:
    print(res[0])
    print(res[1][0], res[1][1], res[1][2])