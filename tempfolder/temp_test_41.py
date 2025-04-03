def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, k = map(int, data[index].split())
        s = list(data[index + 1])
        index += 2
        
        operations = []
        
        # We need to create a balanced bracket sequence with exactly k regular prefixes
        # We will create a sequence of k pairs of '()' and then fill the rest with balanced brackets
        needed = k * 2  # We need 2*k characters for k pairs
        
        # First create the desired sequence
        result = []
        for i in range(k):
            result.append('(')
            result.append(')')
        
        # Now fill the rest with balanced brackets
        for i in range((n // 2) - k):
            result.append('(')
            result.append(')')
        
        # Now result should have length n and be a valid sequence
        result = ''.join(result)
        
        # Now we need to find how to transform s into result using reversals
        s = ''.join(s)
        
        # Find the positions where we need to change s into result
        to_change = []
        for i in range(n):
            if s[i] != result[i]:
                to_change.append(i)
        
        # We will perform reversals
        m = len(to_change) // 2  # We will need m reversals if we have to change m pairs
        
        # The strategy is to pair the indices and reverse the segments
        operations = []
        for i in range(0, len(to_change), 2):
            l = to_change[i]
            r = to_change[i + 1]
            operations.append((l + 1, r + 1))  # Store 1-based indices
        
        # Output the result
        results.append(f"{len(operations)}")
        for op in operations:
            results.append(f"{op[0]} {op[1]}")
    
    print("\n".join(results))

# Example usage:
# Uncomment the next line to run the function with standard input
# solve()