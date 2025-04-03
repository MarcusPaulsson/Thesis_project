def lexicographically_smaller(t, test_cases):
    results = []
    
    for s, c in test_cases:
        n = len(s)
        found = False
        best_name = s
        
        # Check if the original name is already smaller
        if s < c:
            results.append(s)
            continue
        
        # Try to find a valid swap
        for i in range(n):
            for j in range(i + 1, n):
                # Create a new list to swap characters
                new_name = list(s)
                new_name[i], new_name[j] = new_name[j], new_name[i]
                new_name = ''.join(new_name)
                
                # Check if the new name is smaller than c
                if new_name < c:
                    if not found or new_name < best_name:
                        best_name = new_name
                        found = True
        
        results.append(best_name if found else '---')
    
    return results

# Read number of test cases
t = int(input())
test_cases = [input().split() for _ in range(t)]

# Get results
results = lexicographically_smaller(t, test_cases)

# Print results
for result in results:
    print(result)