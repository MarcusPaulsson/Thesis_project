def can_make_equal(t, test_cases):
    results = []
    for i in range(t):
        a, b, c = test_cases[i]
        n = len(a)
        possible = True
        
        for j in range(n):
            if a[j] != b[j]:
                # We need to be able to transform either a[j] or b[j] into the other
                if not ((c[j] == a[j] or c[j] == b[j])):
                    possible = False
                    break
        
        results.append("YES" if possible else "NO")
    
    return results

# Input reading
t = int(input())
test_cases = [tuple(input().strip() for _ in range(3)) for _ in range(t)]

# Get results
results = can_make_equal(t, test_cases)

# Print output
for result in results:
    print(result)