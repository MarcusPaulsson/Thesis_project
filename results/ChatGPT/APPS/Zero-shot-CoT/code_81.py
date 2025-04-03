def can_make_equal(t, test_cases):
    results = []
    for i in range(t):
        a = test_cases[i][0]
        b = test_cases[i][1]
        c = test_cases[i][2]
        
        possible = True
        for j in range(len(a)):
            if a[j] != b[j] and c[j] != a[j] and c[j] != b[j]:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    return results

# Read input
t = int(input().strip())
test_cases = []
for _ in range(t):
    a = input().strip()
    b = input().strip()
    c = input().strip()
    test_cases.append((a, b, c))

# Get results
results = can_make_equal(t, test_cases)

# Print output
for result in results:
    print(result)