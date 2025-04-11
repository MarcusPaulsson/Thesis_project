def is_records_correct(test_cases):
    results = []
    
    for n, records in test_cases:
        valid = True
        previous_p, previous_c = 0, 0
        
        for p, c in records:
            if p < previous_p or c < previous_c or c > p:
                valid = False
                break
            if (p - previous_p) < (c - previous_c):
                valid = False
                break
            
            previous_p, previous_c = p, c
        
        results.append("YES" if valid else "NO")
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Get results
results = is_records_correct(test_cases)

# Print results
for result in results:
    print(result)