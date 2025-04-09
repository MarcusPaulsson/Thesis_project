def is_stats_correct(test_cases):
    results = []
    
    for n, records in test_cases:
        is_correct = True
        prev_plays, prev_clears = 0, 0
        
        for plays, clears in records:
            if plays < prev_plays or clears < prev_clears or clears > plays:
                is_correct = False
                break
            
            # Calculate differences
            plays_diff = plays - prev_plays
            clears_diff = clears - prev_clears
            
            if clears_diff > plays_diff:
                is_correct = False
                break
            
            prev_plays, prev_clears = plays, clears
        
        results.append("YES" if is_correct else "NO")
    
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    records = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, records))

# Get results
results = is_stats_correct(test_cases)

# Output results
print("\n".join(results))