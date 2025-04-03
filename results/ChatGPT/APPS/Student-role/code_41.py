def make_neat_and_clean(t, test_cases):
    results = []
    
    for n, k, s in test_cases:
        operations = []
        # Start by creating a regular sequence with k prefixes
        target = []
        for i in range(k):
            target.append('(')
        for i in range(k):
            target.append(')')
        # Fill the rest with balanced pairs
        for i in range(n // 2 - k):
            target.append('(')
            target.append(')')
        
        target = ''.join(target)

        # Find the operations to convert s to target
        s = list(s)
        for i in range(n):
            if s[i] != target[i]:
                # Find the position to swap with
                for j in range(i + 1, n):
                    if s[j] == target[i]:
                        # Perform the reverse operation
                        operations.append((i + 1, j + 1))
                        s[i:j + 1] = s[i:j + 1][::-1]
                        break
        
        results.append(operations)
    
    # Printing results
    output = []
    for operations in results:
        output.append(str(len(operations)))
        for l, r in operations:
            output.append(f"{l} {r}")
    
    return "\n".join(output)

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Get results and print
print(make_neat_and_clean(t, test_cases))