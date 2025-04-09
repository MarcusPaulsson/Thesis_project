def check_records(test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        records = case[1]
        valid = True
        
        for i in range(1, n):
            p_prev, c_prev = records[i - 1]
            p_curr, c_curr = records[i]
            
            # Check for conditions
            if p_curr < p_prev or c_curr < c_prev or c_curr > p_curr:
                valid = False
                break
            
            # Check the increase in plays and clears
            if p_curr - p_prev < c_curr - c_prev:
                valid = False
                break
        
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