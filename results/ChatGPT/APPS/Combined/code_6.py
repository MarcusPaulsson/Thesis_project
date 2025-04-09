def min_blows_to_defeat_zmei(t, queries):
    results = []

    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        max_effective_damage = 0
        
        for d, h in blows:
            if d >= x:
                # If the blow can defeat Zmei in one hit
                min_blows = 1
                break
            
            effective_damage = d - h
            if effective_damage > 0:
                max_effective_damage = max(max_effective_damage, effective_damage)

        if min_blows == 1:
            results.append(1)
            continue
        
        if max_effective_damage <= 0:
            results.append(-1)
            continue
        
        blows_needed = (x + max_effective_damage - 1) // max_effective_damage
        results.append(blows_needed)
    
    return results

# Read input
t = int(input().strip())
queries = []

for _ in range(t):
    n, x = map(int, input().strip().split())
    blows = [tuple(map(int, input().strip().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Print results
for result in results:
    print(result)