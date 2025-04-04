def min_blows_to_defeat(t, queries):
    results = []
    
    for i in range(t):
        (n, x), blows = queries[i]
        
        max_damage = max(d for d, h in blows)
        min_growth = min(h for d, h in blows)
        
        if max_damage <= min_growth:
            results.append(-1 if max_damage < x else 1)
        else:
            blows_needed = 0
            while x > 0:
                blows_needed += 1
                x = max(0, x - max_damage + min_growth)
            results.append(blows_needed)
    
    return results

# Read input
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append(((n, x), blows))

# Get results
results = min_blows_to_defeat(t, queries)

# Print results
for result in results:
    print(result)