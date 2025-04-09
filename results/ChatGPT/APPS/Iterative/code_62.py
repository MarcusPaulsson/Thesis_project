def min_operations(t, test_cases):
    results = []
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triple = (0, 0, 0)

        # Iterate over possible values for A from 1 up to a + 5
        for A in range(1, a + 6):
            # B should be a multiple of A, calculate the closest multiples
            B1 = (b // A) * A
            B2 = B1 + A
            
            for B in (B1, B2):
                if B < A: continue  # B must be >= A
                # C should be a multiple of B
                C1 = (c // B) * B
                C2 = C1 + B
                
                for C in (C1, C2):
                    if C < B: continue  # C must be >= B
                    
                    # Calculate the total operations needed
                    ops = abs(A - a) + abs(B - b) + abs(C - c)
                    if ops < min_ops:
                        min_ops = ops
                        best_triple = (A, B, C)

        results.append((min_ops, best_triple))

    return results


# Input reading and output
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = min_operations(t, test_cases)

for res in results:
    min_ops, (A, B, C) = res
    print(min_ops)
    print(A, B, C)