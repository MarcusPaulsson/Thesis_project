def min_operations(t, test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triple = (0, 0, 0)
        
        # Iterate over possible values for A
        for A in range(1, a + 1):
            # B must be a multiple of A
            B = ((b + A - 1) // A) * A  # smallest multiple of A >= b
            if B < b:
                B = (b // A) * A  # largest multiple of A <= b
            
            # C must be a multiple of B
            C = ((c + B - 1) // B) * B  # smallest multiple of B >= c
            if C < c:
                C = (c // B) * B  # largest multiple of B <= c
            
            # Calculate operations needed
            ops = abs(A - a) + abs(B - b) + abs(C - c)
            
            if ops < min_ops:
                min_ops = ops
                best_triple = (A, B, C)
        
        results.append((min_ops, best_triple))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = min_operations(t, test_cases)

# Output results
for ops, (A, B, C) in results:
    print(ops)
    print(A, B, C)