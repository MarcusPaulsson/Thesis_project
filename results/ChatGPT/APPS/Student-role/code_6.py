def min_blows_to_defeat(t, queries):
    results = []
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        
        # Find the best blow that reduces heads the most and grows the least
        best_d = 0
        best_h = float('inf')
        
        for d, h in blows:
            if d > best_d or (d == best_d and h < best_h):
                best_d = d
                best_h = h
        
        # If the best blow can defeat Gorynich in one hit
        if best_d >= x:
            results.append(1)
            continue
        
        # If the best blow does not reduce heads enough
        if best_d <= best_h:
            results.append(-1)
            continue
        
        # Calculate the number of blows needed
        # Effective reduction per blow
        effective_reduction = best_d - best_h
        
        # Calculate the number of blows needed to reduce heads to zero
        blows_needed = (x - best_d + effective_reduction - 1) // effective_reduction + 1
        
        results.append(blows_needed)
    
    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat(t, queries)

# Output results
for result in results:
    print(result)