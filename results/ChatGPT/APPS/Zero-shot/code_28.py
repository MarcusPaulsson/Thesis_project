def can_form_abacaba(s, n):
    target = "abacaba"
    occurrences = []
    
    # Check for potential placements of "abacaba"
    for i in range(n - 6):
        substring = s[i:i + 7]
        if all(ss == tt or ss == '?' for ss, tt in zip(substring, target)):
            occurrences.append(i)
    
    # If there are multiple occurrences, we can't have exactly one
    if len(occurrences) > 1:
        return "No"
    
    # If no occurrences, we can replace a '?' with "abacaba"
    if len(occurrences) == 0:
        # Try to place "abacaba" at every possible position
        for i in range(n - 6):
            new_s = list(s)
            for j in range(7):
                new_s[i + j] = target[j]
            # Check if this creates exactly one occurrence
            if new_s.count('a') >= 3 and new_s.count('b') >= 1 and new_s.count('c') >= 1:
                new_s = ''.join(new_s)
                # Fill remaining '?' with 'z' or any other letter
                new_s = new_s.replace('?', 'z')
                if new_s.count('abacaba') == 1:
                    return f"Yes\n{new_s}"
        return "No"

    # If exactly one occurrence is found, we need to ensure the rest are handled
    index = occurrences[0]
    new_s = list(s)
    for j in range(7):
        new_s[index + j] = target[j]
    new_s = ''.join(new_s)
    
    # Replace remaining '?' with 'z' or any other letter
    new_s = new_s.replace('?', 'z')
    
    # Verify that "abacaba" occurs exactly once
    if new_s.count('abacaba') == 1:
        return f"Yes\n{new_s}"
    else:
        return "No"

T = int(input())
results = []
for _ in range(T):
    n = int(input().strip())
    s = input().strip()
    results.append(can_form_abacaba(s, n))

print("\n".join(results))