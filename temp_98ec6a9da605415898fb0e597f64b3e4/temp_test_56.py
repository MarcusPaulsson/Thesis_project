def min_blows_to_defeat(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blow_needed = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                min_blow_needed = 1
                possible = True
            else:
                # Calculate the effective damage and growth
                effective_damage = d - h
                if effective_damage > 0:
                    # Calculate how many blows are needed to reduce heads below 0
                    remaining_heads = x - d
                    # Calculate full rounds of effective damage needed
                    rounds_needed = (remaining_heads + effective_damage - 1) // effective_damage
                    blows_needed = rounds_needed + 1  # +1 for the initial blow
                    min_blow_needed = min(min_blow_needed, blows_needed)
                    possible = True
        
        results.append(min_blow_needed if possible else -1)
    
    return results

# Read input
t = int(input())
queries = []

for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat(t, queries)

# Print results
for result in results:
    print(result)