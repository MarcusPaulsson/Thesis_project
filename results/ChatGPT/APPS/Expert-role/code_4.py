def beautiful_numbers(t, test_cases):
    results = []
    
    for n, p in test_cases:
        beautiful = ['0'] * n
        max_seen = 0
        
        for i in range(n):
            max_seen = max(max_seen, p[i])
            if max_seen == i + 1:
                beautiful[i] = '1'
        
        results.append(''.join(beautiful))
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Get results and print
results = beautiful_numbers(t, test_cases)
for result in results:
    print(result)