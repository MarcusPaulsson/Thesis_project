def min_blows_to_defeat_monster(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        
        # Calculate effective damage and head growth
        effective_blows = []
        for d, h in blows:
            if d >= x:  # Can defeat the monster in one blow
                effective_blows.append((x, 0))  # One blow to defeat
            else:  # Not enough to defeat, calculate net effect
                effective_blows.append((d, h))
        
        # Find the best blow combination
        for d, h in effective_blows:
            if h < d:  # If the heads grown back are less than the damage dealt
                # Calculate how many blows are necessary to reach zero heads
                blows_needed = (x + (d - h) - 1) // (d - h)  # ceil(x / (d - h))
                min_blows = min(min_blows, blows_needed)
            elif h == d:
                # If growth is equal to damage, we can only defeat if we can deal full damage
                if x % d == 0:
                    blows_needed = x // d
                    min_blows = min(min_blows, blows_needed)
        
        # Check if there's a blow that can defeat the monster immediately
        if min_blows == float('inf'):
            results.append(-1)
        else:
            results.append(min_blows)
    
    return results

# Read input
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat_monster(t, queries)

# Print results
for result in results:
    print(result)