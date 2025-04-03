def minimal_crossroad(t, test_cases):
    results = []
    
    for a, b, p, s in test_cases:
        total_cost = 0
        n = len(s)
        i = 0
        
        while i < n - 1:
            if s[i] == 'A':
                while i < n - 1 and s[i] == 'A':
                    i += 1
                total_cost += a
            else:
                while i < n - 1 and s[i] == 'B':
                    i += 1
                total_cost += b
            
            if total_cost > p:
                break
        
        results.append(i + 1)  # +1 for 1-based index
        
    return results


# Read input
t = int(input())
test_cases = []

for _ in range(t):
    a, b, p = map(int, input().split())
    s = input().strip()
    test_cases.append((a, b, p, s))

# Get results
results = minimal_crossroad(t, test_cases)

# Print results
for result in results:
    print(result)