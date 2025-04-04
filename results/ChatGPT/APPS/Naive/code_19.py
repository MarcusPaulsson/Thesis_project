def is_records_correct(test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        records = case[1]
        
        valid = True
        prev_p, prev_c = 0, 0
        
        for i in range(n):
            p, c = records[i]
            
            if p < prev_p or c < prev_c or c > p:
                valid = False
                break
            
            if i > 0:
                if p - prev_p < c - prev_c:
                    valid = False
                    break
            
            prev_p, prev_c = p, c
        
        results.append("YES" if valid else "NO")

    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Getting results
results = is_records_correct(test_cases)

# Output results
for result in results:
    print(result)