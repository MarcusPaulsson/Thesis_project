def minimize_f(t, test_cases):
    results = []
    
    for n, T, a in test_cases:
        count = {}
        colors = [0] * n
        
        for i in range(n):
            count[a[i]] = count.get(a[i], 0) + 1
        
        for i in range(n):
            complement = T - a[i]
            if complement in count:
                if complement == a[i]:
                    # If the element is its own complement, we should alternate colors
                    colors[i] = 1 if count[a[i]] % 2 == 0 else 0
                else:
                    # We can assign colors based on the counts
                    if count[a[i]] >= count[complement]:
                        colors[i] = 0  # Paint the more frequent color to white
                    else:
                        colors[i] = 1  # Paint the less frequent color to black
            
        results.append(' '.join(map(str, colors)))
    
    return results

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, T, a))

# Get results
results = minimize_f(t, test_cases)

# Output results
for result in results:
    print(result)