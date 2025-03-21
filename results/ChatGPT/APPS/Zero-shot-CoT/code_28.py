def can_form_abacaba(s):
    target = "abacaba"
    n = len(s)
    positions = []
    
    # Check all possible positions for "abacaba"
    for i in range(n - 6):
        # Check if we can fit "abacaba" in current position
        can_fit = True
        for j in range(7):
            if s[i + j] != '?' and s[i + j] != target[j]:
                can_fit = False
                break
        if can_fit:
            positions.append(i)
    
    # Try to mark one occurrence of "abacaba"
    for pos in positions:
        # Create a copy of string to modify
        modified = list(s)
        # Place "abacaba" at position pos
        for j in range(7):
            modified[pos + j] = target[j]
        
        # Replace remaining '?' with any character (e.g. 'z')
        for k in range(n):
            if modified[k] == '?':
                modified[k] = 'z'
        
        # Check if "abacaba" occurs exactly once
        result_str = ''.join(modified)
        if result_str.count(target) == 1:
            return "Yes", result_str
    
    return "No", None

# Read number of test cases
T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    result, modified_str = can_form_abacaba(s)
    print(result)
    if modified_str:
        print(modified_str)