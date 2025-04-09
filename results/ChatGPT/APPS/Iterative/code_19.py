def check_stats(test_cases):
    results = []
    for case in test_cases:
        n, stats = case
        valid = True
        
        for i in range(n):
            p_i, c_i = stats[i]
            if (i > 0):
                p_prev, c_prev = stats[i - 1]
                
                # Check if plays or clears have decreased
                if p_i < p_prev or c_i < c_prev:
                    valid = False
                    break
                
                # Check if clears exceed plays
                if c_i > p_i:
                    valid = False
                    break
                
                # Check if the increase in clears is valid
                if p_i - p_prev < c_i - c_prev:
                    valid = False
                    break
        
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
results = check_stats(test_cases)

# Print output
for result in results:
    print(result)