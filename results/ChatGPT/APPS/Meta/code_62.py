def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triple = (a, b, c)
        
        # Check for all possible values of A
        for A in range(1, a + 1):
            # B should be a multiple of A
            B = ((b + A - 1) // A) * A  # smallest multiple of A >= b
            if B < b:
                B += A  # ensure B is at least b
            
            # C should be a multiple of B
            C = ((c + B - 1) // B) * B  # smallest multiple of B >= c
            if C < c:
                C += B  # ensure C is at least c
            
            # Calculate the number of moves
            moves = (A - a) + (B - b) + (C - c)
            if moves < min_moves:
                min_moves = moves
                best_triple = (A, B, C)
        
        results.append((min_moves, best_triple))
    
    return results

# Example usage
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = min_operations(t, test_cases)

for moves, (A, B, C) in results:
    print(moves)
    print(A, B, C)