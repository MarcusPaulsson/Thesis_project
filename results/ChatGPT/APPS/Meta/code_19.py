def is_records_correct(test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        stats = case[1]
        
        valid = True
        previous_p = 0
        previous_c = 0
        
        for p, c in stats:
            if p < previous_p or c < previous_c or c > p:
                valid = False
                break
            
            if c - previous_c > p - previous_p:
                valid = False
                break
            
            previous_p = p
            previous_c = c
        
        results.append("YES" if valid else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results
results = is_records_correct(test_cases)

# Print results
for result in results:
    print(result)