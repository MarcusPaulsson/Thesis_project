def lexicographically_smaller(t, test_cases):
    results = []
    
    for s, c in test_cases:
        if s < c:
            results.append(s)
            continue
        
        found = False
        s_list = list(s)
        n = len(s_list)
        
        # Iterate through each character and try to find a smaller swap
        for i in range(n):
            for j in range(i + 1, n):
                # Swap characters at position i and j
                s_list[i], s_list[j] = s_list[j], s_list[i]
                new_name = ''.join(s_list)
                if new_name < c:
                    results.append(new_name)
                    found = True
                    break
                # Swap back to restore original s_list
                s_list[i], s_list[j] = s_list[j], s_list[i]
            if found:
                break
        
        if not found:
            results.append("---")
    
    return results

# Input reading
t = int(input())
test_cases = [input().strip().split() for _ in range(t)]

# Get results
results = lexicographically_smaller(t, test_cases)

# Output results
for result in results:
    print(result)