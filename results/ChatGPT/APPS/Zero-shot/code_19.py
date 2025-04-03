def check_records(test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        records = case[1]
        
        valid = True
        previous_plays, previous_clears = 0, 0
        
        for p, c in records:
            if p < previous_plays or c < previous_clears or c > p:
                valid = False
                break
            
            if p - previous_plays < c - previous_clears:
                valid = False
                break
            
            previous_plays, previous_clears = p, c
        
        results.append("YES" if valid else "NO")
    
    return results

# Reading input
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Checking records
results = check_records(test_cases)

# Printing results
for result in results:
    print(result)