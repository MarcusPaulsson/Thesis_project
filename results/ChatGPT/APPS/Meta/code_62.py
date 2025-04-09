def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triplet = (0, 0, 0)

        # Iterate over possible A values (from 1 to a)
        for A in range(1, a + 1):
            # Iterate over possible B values (multiples of A)
            for k in range(1, c // A + 1):
                B = A * k
                if B < b:
                    continue

                if B > c:
                    break

                # Find the closest C that is a multiple of B
                for m in range(1, c // B + 1):
                    C = B * m
                    if C < b:
                        continue

                    if C > c:
                        break

                    # Calculate the number of moves required
                    moves = abs(a - A) + abs(b - B) + abs(c - C)

                    if moves < min_moves:
                        min_moves = moves
                        best_triplet = (A, B, C)

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