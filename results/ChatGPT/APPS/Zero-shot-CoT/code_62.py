def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triplet = (0, 0, 0)

        # Iterate through possible values for A
        for A in range(1, 10001):  # A can be from 1 to 10000
            # B must be a multiple of A
            B = ((b + A - 1) // A) * A  # smallest multiple of A >= b
            if B < b:
                B += A  # ensure B is at least b
            
            # C must be a multiple of B
            C = ((c + B - 1) // B) * B  # smallest multiple of B >= c
            if C < c:
                C += B  # ensure C is at least c

            # Calculate the number of operations
            operations = max(0, A - a) + max(0, B - b) + max(0, C - c)
            
            # Check if the operations are minimal
            if operations < min_moves:
                min_moves = operations
                best_triplet = (A, B, C)

        results.append((min_moves, best_triplet))
    
    return results

# Input reading and function execution
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = min_operations(t, test_cases)

# Output results
for moves, (A, B, C) in results:
    print(moves)
    print(A, B, C)