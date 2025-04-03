def process_test_cases(t, test_cases):
    results = []
    for case in test_cases:
        n, k, s = case
        operations = []
        
        # Target: We want k regular prefixes
        # We will create a string that has k regular prefixes 
        # and the rest of the string will be balanced but can have
        # an arbitrary structure.
        
        target = []
        for i in range(k):
            target.append('(')
        for i in range(k):
            target.append(')')
        
        # Fill the rest of the string with remaining parentheses
        for i in range(n // 2 - k):
            target.append('(')
            target.append(')')
        
        target = ''.join(target)
        
        # If the current string is not equal to the target, we will perform operations
        if s != target:
            s_list = list(s)
            # The target string is constructed and we need to match s_list to it
            
            for i in range(n):
                if s_list[i] != target[i]:
                    # Find where the target character is in s_list
                    for j in range(i + 1, n):
                        if s_list[j] == target[i]:
                            # We found a character to swap
                            # Reverse the segment from i to j
                            operations.append((i + 1, j + 1))  # Store 1-based indices
                            s_list[i:j + 1] = reversed(s_list[i:j + 1])
                            break
        
        results.append((len(operations), operations))
    
    return results


# Read input
t = int(input().strip())
test_cases = []

for _ in range(t):
    n, k = map(int, input().strip().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Process test cases
results = process_test_cases(t, test_cases)

# Output results
for res in results:
    m, ops = res
    print(m)
    for op in ops:
        print(op[0], op[1])