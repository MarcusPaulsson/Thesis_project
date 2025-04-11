def check_records(test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        records = case[1]
        valid = True
        
        for i in range(n):
            p_i, c_i = records[i]
            if i > 0:
                p_prev, c_prev = records[i - 1]
                if p_i < p_prev or c_i < c_prev or c_i > p_i:
                    valid = False
                    break
                if (p_i - p_prev) < (c_i - c_prev):
                    valid = False
                    break
        
        results.append("YES" if valid else "NO")
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    n = int(input())
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Check records and print results
results = check_records(test_cases)
for result in results:
    print(result)