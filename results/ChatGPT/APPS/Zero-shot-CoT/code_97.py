def find_better_names(t, test_cases):
    results = []
    
    for s, c in test_cases:
        original_s = s
        found = False
        
        # Check if original string is already smaller
        if s < c:
            results.append(s)
            continue
        
        # Convert string to list for easier manipulation
        s_list = list(s)
        n = len(s_list)
        
        for i in range(n):
            for j in range(i + 1, n):
                # Swap characters at index i and j
                s_list[i], s_list[j] = s_list[j], s_list[i]
                new_s = ''.join(s_list)
                
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

# Example usage
t = int(input())
test_cases = [input().split() for _ in range(t)]
results = find_better_names(t, test_cases)
for result in results:
    print(result)