def has_palindrome_subsequence(t, test_cases):
    results = []
    
    for n, a in test_cases:
        last_seen = {}
        found = False
        
        for i in range(n):
            if a[i] in last_seen:
                # Check if the distance between the same elements is at least 2
                if i - last_seen[a[i]] >= 2:
                    found = True
                    break
            last_seen[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results