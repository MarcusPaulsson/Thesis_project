def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_a, best_b, best_c = 0, 0, 0
        
        # Loop through possible values for A
        for A in range(1, a + 2):
            # For a fixed A, calculate B and C that satisfy the conditions
            if A > 0:
                B = ((b + A - 1) // A) * A  # smallest B >= b and divisible by A
                C = ((c + B - 1) // B) * B  # smallest C >= c and divisible by B
                
                ops = abs(A - a) + abs(B - b) + abs(C - c)
                
                if ops < min_ops:
                    min_ops = ops
                    best_a, best_b, best_c = A, B, C
        
        results.append((min_ops, best_a, best_b, best_c))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for res in results:
    print(res[0])
    print(res[1], res[2], res[3])