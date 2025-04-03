def can_make_equal(t, test_cases):
    results = []
    for i in range(t):
        a, b, c = test_cases[i]
        n = len(a)
        possible = True
        
        for j in range(n):
            if a[j] != b[j]:
                # Check if we can swap with c[j]
                if c[j] != a[j] and c[j] != b[j]:
                    possible = False
                    break
        
        results.append("YES" if possible else "NO")
    
    return results

# Read input
t = int(input())
test_cases = [tuple(input().strip() for _ in range(3)) for _ in range(t)]

# Get results
results = can_make_equal(t, test_cases)

# Print results
for result in results:
    print(result)