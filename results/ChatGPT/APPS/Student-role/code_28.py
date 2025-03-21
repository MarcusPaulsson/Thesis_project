def can_form_unique_abacaba(test_cases):
    target = "abacaba"
    results = []
    
    for n, s in test_cases:
        # Attempt to place "abacaba" in the string
        found_positions = []
        
        for i in range(n - 6):
            if all(s[i + j] in (target[j], '?') for j in range(7)):
                found_positions.append(i)
        
        # Try to place "abacaba" in each found position and check
        for pos in found_positions:
            modified_s = list(s)  # Work with a mutable list
            for j in range(7):
                modified_s[pos + j] = target[j]
            
            # Replace remaining '?' with 'z' (or any other letter)
            modified_s = ['z' if x == '?' else x for x in modified_s]
            modified_s = ''.join(modified_s)
            
            # Check if "abacaba" occurs exactly once
            if modified_s.count(target) == 1:
                results.append("Yes")
                results.append(modified_s)
                break
        else:
            results.append("No")
    
    return results

# Read input
T = int(input())
test_cases = [(int(input()), input().strip()) for _ in range(T)]

# Get results
results = can_form_unique_abacaba(test_cases)

# Print results
for result in results:
    print(result)