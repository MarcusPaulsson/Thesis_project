def min_operations_to_divisible_triplet(test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triplet = (a, b, c)

        # Iterate over possible values for A
        for A in range(1, a + 1):
            # Calculate the nearest multiples of A for B and C
            B = ((b + A - 1) // A) * A  # Next multiple of A >= b
            if B < b:
                B = (b // A) * A  # Previous multiple of A <= b
            
            C = ((c + B - 1) // B) * B  # Next multiple of B >= c
            if C < c:
                C = (c // B) * B  # Previous multiple of B <= c
            
            # Calculate operations needed
            operations = abs(A - a) + abs(B - b) + abs(C - c)
            
            # Update minimum operations and best triplet
            if operations < min_operations:
                min_operations = operations
                best_triplet = (A, B, C)

        results.append((min_operations, best_triplet))
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations_to_divisible_triplet(test_cases)

# Print output
for operations, triplet in results:
    print(operations)
    print(*triplet)