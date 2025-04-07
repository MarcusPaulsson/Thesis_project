def is_stats_correct(test_cases):
    results = []
    for stats in test_cases:
        n = stats[0]
        plays_and_clears = stats[1]
        
        valid = True
        prev_p, prev_c = 0, 0
        
        for p, c in plays_and_clears:
            if p < prev_p or c < prev_c or c > p:
                valid = False
                break
            if (c - prev_c) > (p - prev_p):
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
    plays_and_clears = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, plays_and_clears))

results = is_stats_correct(test_cases)

# Output results
for result in results:
    print(result)