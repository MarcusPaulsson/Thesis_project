def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        
        # Determine the best blow
        effective_blows = []
        for d, h in blows:
            if d > 0:
                effective_blows.append((d, h))
        
        # If no effective blows, Zmei can't be defeated
        if not effective_blows:
            results.append(-1)
            continue
        
        # Find the minimum blows needed
        for d, h in effective_blows:
            # Calculate the net effect of this blow
            net_effect = d - h
            if net_effect >= 0:
                # If the blow does not reduce heads effectively
                if x <= d:
                    # We can defeat Gorynich in one blow
                    min_blows = min(min_blows, 1)
            else:
                # Calculate how many blows are needed
                blows_needed = (x + net_effect - 1) // net_effect
                if blows_needed >= 0:
                    min_blows = min(min_blows, blows_needed)

        if min_blows == float('inf'):
            results.append(-1)
        else:
            results.append(min_blows)

    return results

# Reading input
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Getting results
results = min_blows_to_defeat_zmei(t, queries)

# Printing results
for result in results:
    print(result)