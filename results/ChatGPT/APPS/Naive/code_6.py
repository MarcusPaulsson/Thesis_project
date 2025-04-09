def min_blows_to_defeat(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query['n'], query['x'], query['blows']
        min_blows = float('inf')
        
        for d, h in blows:
            if d >= x:
                min_blows = min(min_blows, 1)
                continue
            
            # Calculate effective damage and heads produced
            effective_damage = d - h
            if effective_damage <= 0:
                continue
            
            # Calculate number of blows required
            blows_needed = (x - d + effective_damage - 1) // effective_damage + 1
            min_blows = min(min_blows, blows_needed)
        
        results.append(min_blows if min_blows != float('inf') else -1)
    
    return results

# Read input
t = int(input())
queries = []

for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append({'n': n, 'x': x, 'blows': blows})

# Get results
results = min_blows_to_defeat(t, queries)

# Print outputs
for result in results:
    print(result)