def beautiful_numbers(t, test_cases):
    results = []
    for n, p in test_cases:
        beautiful = ['0'] * n
        max_value = 0
        
        for i in range(n):
            max_value = max(max_value, p[i])
            if max_value == i + 1:
                beautiful[i] = '1'
        
        results.append(''.join(beautiful))
    
    return results

# Input Reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Process and Output
results = beautiful_numbers(t, test_cases)
for result in results:
    print(result)