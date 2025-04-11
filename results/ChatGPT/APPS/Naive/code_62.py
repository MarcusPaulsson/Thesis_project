def min_operations_to_divisible_triplet(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triplet = (0, 0, 0)
        
        # Iterate over possible values for A
        for A in range(1, a + 1):
            # Calculate the nearest B that is divisible by A
            if b % A == 0:
                B = b
            else:
                B = (b // A + 1) * A
            
            # Calculate the nearest C that is divisible by B
            if C % B == 0:
                C = c
            else:
                C = (c // B + 1) * B
            
            # Calculate operations needed
            operations = abs(A - a) + abs(B - b) + abs(C - c)
            
            if operations < min_operations:
                min_operations = operations
                best_triplet = (A, B, C)
        
        results.append((min_operations, best_triplet))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations_to_divisible_triplet(t, test_cases)

# Output results
for operations, triplet in results:
    print(operations)
    print(*triplet)