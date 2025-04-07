def min_operations(test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triplet = (a, b, c)

        # A can be 1 to a+1 (inclusive)
        for A in range(1, a + 2):
            # B can be A to c (inclusive)
            for B in range(A, c + 1):
                # C can be B to c (inclusive) and must be a multiple of B
                C = (B * ((c + B - 1) // B))  # smallest multiple of B >= c
                if C < B:
                    continue
                
                # Calculate the number of operations needed
                operations = abs(A - a) + abs(B - b) + abs(C - c)
                if operations < min_operations:
                    min_operations = operations
                    best_triplet = (A, B, C)

        results.append((min_operations, best_triplet))
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(test_cases)

# Print output
for operations, (A, B, C) in results:
    print(operations)
    print(A, B, C)