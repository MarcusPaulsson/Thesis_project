def is_valid_record(n, stats):
    previous_plays = previous_clears = 0
    
    for plays, clears in stats:
        if plays < previous_plays or clears < previous_clears or clears > plays:
            return False
        if (plays - previous_plays) < (clears - previous_clears):
            return False
        
        previous_plays, previous_clears = plays, clears
    
    return True

def check_records(test_cases):
    results = []
    
    for n, stats in test_cases:
        valid = is_valid_record(n, stats)
        results.append("YES" if valid else "NO")
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, stats))

# Get results and print them
results = check_records(test_cases)
print("\n".join(results))