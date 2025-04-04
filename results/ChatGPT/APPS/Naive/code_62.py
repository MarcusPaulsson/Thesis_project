def min_operations(t, cases):
    results = []
    
    for a, b, c in cases:
        # Initialize the minimum operations and best triplet
        min_ops = float('inf')
        best_triplet = (0, 0, 0)
        
        # Iterate through possible values of A
        for A in range(1, a + 1):
            # B must be a multiple of A, so we can find suitable B
            B = A
            while B < b or B % A != 0:
                B += 1
            
            # C must be a multiple of B
            C = B
            while C < c or C % B != 0:
                C += 1
            
            # Calculate operations needed to reach A, B, C
            operations = (abs(a - A) + abs(b - B) + abs(c - C))
            
            # Update minimum operations and best triplet found
            if operations < min_ops:
                min_ops = operations
                best_triplet = (A, B, C)
        
        results.append((min_ops, best_triplet))
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]
    
    results = min_operations(t, cases)
    for ops, (A, B, C) in results:
        print(ops)
        print(A, B, C)

if __name__ == "__main__":
    main()