def min_operations(test_cases):
    results = []
    for a, b, c in test_cases:
        min_ops = float('inf')
        best_triplet = (0, 0, 0)
        
        for A in range(1, 10001):
            for B in range(A, 10001, A):
                for C in range(B, 10001, B):
                    ops = abs(A - a) + abs(B - b) + abs(C - c)
                    if ops < min_ops:
                        min_ops = ops
                        best_triplet = (A, B, C)

        results.append((min_ops, best_triplet))
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Processing the test cases
results = min_operations(test_cases)

# Output results
for ops, triplet in results:
    print(ops)
    print(*triplet)