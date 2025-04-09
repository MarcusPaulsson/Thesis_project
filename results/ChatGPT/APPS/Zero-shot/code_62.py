def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triple = (0, 0, 0)
        
        for A in range(1, c + 1):
            if A > a:
                moves_a = A - a
            else:
                moves_a = a - A
            
            if A > 0:
                # B should be a multiple of A
                B = ((b + A - 1) // A) * A  # smallest multiple of A >= b
                moves_b = abs(B - b)
            else:
                B = 1
                moves_b = abs(B - b)
            
            # C should be a multiple of B
            C = ((c + B - 1) // B) * B  # smallest multiple of B >= c
            moves_c = abs(C - c)
            
            total_moves = moves_a + moves_b + moves_c
            
            if total_moves < min_moves:
                min_moves = total_moves
                best_triple = (A, B, C)
        
        results.append((min_moves, best_triple))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Getting results
results = min_operations(t, test_cases)

# Output results
for res in results:
    print(res[0])
    print(*res[1])