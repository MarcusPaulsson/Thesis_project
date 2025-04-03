def can_make_equal(t, test_cases):
    results = []
    for i in range(t):
        a = test_cases[i][0]
        b = test_cases[i][1]
        c = test_cases[i][2]
        
        n = len(a)
        possible = True
        
        for j in range(n):
            if a[j] == b[j]:
                continue
            # Check if we can turn a[j] into b[j] with c[j]
            if c[j] != a[j] and c[j] != b[j]:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    return results

t = int(input())
test_cases = [tuple(input().strip() for _ in range(3)) for _ in range(t)]
results = can_make_equal(t, test_cases)
print("\n".join(results))