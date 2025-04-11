def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triple = (0, 0, 0)

        # Iterate over possible values for A
        for A in range(1, a + 1):
            # Find the closest B that is divisible by A
            if b % A == 0:
                B = b
            else:
                B = (b // A + 1) * A
            
            # Find the closest C that is divisible by B
            if C % B == 0:
                C = c
            else:
                C = (c // B + 1) * B
            
            # Calculate the number of operations needed
            moves = abs(A - a) + abs(B - b) + abs(C - c)
            
            if moves < min_moves:
                min_moves = moves
                best_triple = (A, B, C)

        results.append((min_moves, best_triple))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for moves, (A, B, C) in results:
    print(moves)
    print(A, B, C)