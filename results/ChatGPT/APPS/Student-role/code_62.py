def min_operations(test_cases):
    results = []
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triple = (a, b, c)

        # Check all possible values for A, B, C
        for A in range(1, 10001):
            for B in range(A, 10001):
                if B % A == 0:
                    for C in range(B, 10001):
                        if C % B == 0:
                            operations = abs(A - a) + abs(B - b) + abs(C - c)
                            if operations < min_operations:
                                min_operations = operations
                                best_triple = (A, B, C)

        results.append((min_operations, best_triple))

    return results


t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = min_operations(test_cases)

for res in results:
    print(res[0])
    print(res[1][0], res[1][1], res[1][2])