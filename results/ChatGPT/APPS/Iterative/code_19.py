def check_records(test_cases):
    results = []
    for case in test_cases:
        n, records = case
        valid = True
        prev_p, prev_c = 0, 0
        
        for p, c in records:
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
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Get results and print them
results = check_records(test_cases)
for result in results:
    print(result)