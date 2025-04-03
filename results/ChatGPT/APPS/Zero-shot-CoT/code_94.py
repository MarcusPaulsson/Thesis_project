def paint_array(t, test_cases):
    results = []
    for n, T, a in test_cases:
        color = [0] * n
        count = {}
        
        for i in range(n):
            count[a[i]] = count.get(a[i], 0) + 1
        
        for i in range(n):
            complement = T - a[i]
            if complement in count:
                if count[complement] > 0:
                    if a[i] != complement:
                        color[i] = 1  # Paint this one black
                        count[a[i]] -= 1
                    else:
                        # If they're the same, we can alternate colors
                        color[i] = 1 if count[a[i]] % 2 == 0 else 0
                        count[a[i]] -= 1
        
        results.append(' '.join(map(str, color)))
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, T, a))

# Get results
results = paint_array(t, test_cases)

# Print output
for res in results:
    print(res)