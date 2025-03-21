def can_transform(t, test_cases):
    results = []
    for n, a, b in test_cases:
        can_increase = can_decrease = False
        possible = True
        
        for i in range(n):
            if a[i] == 1:
                can_increase = True
            if a[i] == -1:
                can_decrease = True
            
            if b[i] > a[i] and not can_increase:
                possible = False
                break
            if b[i] < a[i] and not can_decrease:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Process and output results
results = can_transform(t, test_cases)
print("\n".join(results))