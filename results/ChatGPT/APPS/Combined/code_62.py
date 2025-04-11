def min_operations_to_divisible_triplet(test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triplet = (a, b, c)
        
        # Iterate through possible values for A
        for A in range(1, a + 1):
            # Find the closest B that is divisible by A
            B = (b // A) * A if b % A == 0 else ((b // A) + 1) * A
            
            # Ensure B is at least A
            if B < A:
                B = A
            
            # Find the closest C that is divisible by B
            C = (c // B) * B if c % B == 0 else ((c // B) + 1) * B
            
            # Ensure C is at least B
            if C < B:
                C = B
            
            # Calculate the number of operations
            operations = abs(A - a) + abs(B - b) + abs(C - c)
            
            # Update if we found a better solution
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