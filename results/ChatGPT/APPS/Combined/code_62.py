def min_operations_to_divisible_triplet(test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_operations = float('inf')
        best_triplet = (a, b, c)

        # We will iterate over possible values for A, B, and C
        for A in range(1, a + 2):  # A can be from 1 to a+1
            for B in range(A, c + 2):  # B can be from A to c+1
                if B % A == 0:  # Check if B is divisible by A
                    # Find the nearest C such that C is a multiple of B and C >= B
                    C = (c // B) * B
                    if C < B:
                        C += B
                    
                    if C > c:  # Ensure C does not exceed the original c
                        C = (c // B + 1) * B
                    
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
results = min_operations_to_divisible_triplet(test_cases)

# Print output
for operations, (A, B, C) in results:
    print(operations)
    print(A, B, C)