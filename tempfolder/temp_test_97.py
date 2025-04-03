def lexicographically_smaller(t, test_cases):
    results = []
    
    for s, c in test_cases:
        n = len(s)
        found = False
        s_list = list(s)
        
        # Check if the original string is already smaller
        if s < c:
            results.append(s)
            continue
        
        # Try to find a valid swap
        for i in range(n):
            for j in range(i + 1, n):
                # Swap characters at positions i and j
                s_list[i], s_list[j] = s_list[j], s_list[i]
                new_s = ''.join(s_list)
                
                # Check if the new string is smaller than c
                if new_s < c:
                    results.append(new_s)
                    found = True
                    break
                
                # Swap back
                s_list[i], s_list[j] = s_list[j], s_list[i]
                
            if found:
                break
        
        if not found:
            results.append("---")
    
    return results


# Input reading
t = int(input().strip())
test_cases = [input().strip().split() for _ in range(t)]
results = lexicographically_smaller(t, test_cases)

# Output results
for result in results:
    print(result)