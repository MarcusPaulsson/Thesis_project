def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triplet = (a, b, c)

        # Check for all possible A, B, C combinations
        for A in range(1, a + 1):
            for B in range(A, c + 1):
                if B % A == 0:
                    C = B
                    while C <= 10000:
                        moves = abs(A - a) + abs(B - b) + abs(C - c)
                        if moves < min_moves:
                            min_moves = moves
                            best_triplet = (A, B, C)
                        C += B
        
        results.append((min_moves, best_triplet))
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Print output
for moves, triplet in results:
    print(moves)
    print(*triplet)