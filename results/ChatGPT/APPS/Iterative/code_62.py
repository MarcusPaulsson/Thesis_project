def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triplet = (0, 0, 0)

        # Iterate over possible values for A
        for A in range(1, a + 1):
            # Iterate over possible values for B that are multiples of A
            for B in range(max(A, b), c + 1):
                if B % A == 0:
                    # Iterate over possible values for C that are multiples of B
                    for C in range(max(B, c), c + 1):
                        if C % B == 0:
                            moves = abs(A - a) + abs(B - b) + abs(C - c)
                            if moves < min_moves:
                                min_moves = moves
                                best_triplet = (A, B, C)

        results.append((min_moves, best_triplet))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for moves, triplet in results:
    print(moves)
    print(*triplet)