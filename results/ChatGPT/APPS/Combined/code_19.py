def is_records_correct(test_cases):
    results = []
    
    for n, stats in test_cases:
        valid = True
        prev_p, prev_c = 0, 0
        
        for p, c in stats:
            if p < prev_p or c < prev_c or c > p:
                valid = False
                break
            if (p - prev_p) < (c - prev_c):
                valid = False
                break
            
            prev_p, prev_c = p, c
        
        results.append("YES" if valid else "NO")
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results
results = is_records_correct(test_cases)

# Print results
for result in results:
    print(result)