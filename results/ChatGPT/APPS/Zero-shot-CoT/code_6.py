def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        
        # Check if there's a blow that can defeat Zmei Gorynich in one hit
        for d, h in blows:
            if d >= x:
                min_blows = 1
        
        # Calculate the minimum blows needed if Zmei can be defeated
        for d, h in blows:
            if d < x:  # Only consider blows that will not defeat Zmei in one hit
                # Effective damage done after growth
                effective_damage = d - h
                if effective_damage <= 0:
                    continue  # This blow won't help at all
                
                # Calculate the blows needed
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
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Print results
for result in results:
    print(result)