def is_stats_correct(test_cases):
    results = []
    
    for case in test_cases:
        n, stats = case
        valid = True
        
        for i in range(1, n):
            p_prev, c_prev = stats[i-1]
            p_curr, c_curr = stats[i]
            
            # Check for non-decreasing plays and clears
            if p_curr < p_prev or c_curr < c_prev:
                valid = False
                break
            
            # Check if clears do not exceed plays
            if c_curr > p_curr:
                valid = False
                break
            
            # Check the increase in plays and clears
            if (c_curr - c_prev) > (p_curr - p_prev):
                valid = False
                break
            
        # Check the first entry
        p_first, c_first = stats[0]
        if c_first > p_first:
            valid = False
            
        results.append("YES" if valid else "NO")
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results and print
results = is_stats_correct(test_cases)
for result in results:
    print(result)