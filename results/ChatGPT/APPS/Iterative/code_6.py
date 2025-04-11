def min_blows_to_defeat_zmei(t, queries):
    results = []
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                min_blows = min(min_blows, 1)
                possible = True
            else:
                # Calculate the effective damage per blow
                effective_damage = d - h
                if effective_damage > 0:
                    # Calculate how many blows are needed to reduce heads to zero
                    blows_needed = (x - d + effective_damage - 1) // effective_damage + 1
                    min_blows = min(min_blows, blows_needed)
                    possible = True
        
        if possible:
            results.append(min_blows)
        else:
            results.append(-1)
    
    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Output results
for result in results:
    print(result)