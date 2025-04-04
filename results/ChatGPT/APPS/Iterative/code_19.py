def check_records(test_cases):
    results = []
    
    for n, stats in test_cases:
        valid = True
        
        for i in range(1, n):
            p, c = stats[i]
            prev_p, prev_c = stats[i - 1]
            if p < prev_p or c < prev_c or c > p or c - prev_c > p - prev_p:
                valid = False
                break
        
        results.append("YES" if valid else "NO")
    
    return results

# Read input
T = int(input().strip())
test_cases = []

for _ in range(T):
    n = int(input().strip())
    stats = [tuple(map(int, input().strip().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results
results = check_records(test_cases)

# Print results
print("\n".join(results))