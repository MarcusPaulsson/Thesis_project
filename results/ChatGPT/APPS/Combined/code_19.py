def is_records_correct(test_cases):
    results = []
    
    for n, stats in test_cases:
        valid = True
        
        for i in range(1, n):
            p_prev, c_prev = stats[i - 1]
            p_i, c_i = stats[i]
            
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
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results and print
results = is_records_correct(test_cases)
print("\n".join(results))