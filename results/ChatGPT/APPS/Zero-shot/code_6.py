def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x = query[0]
        blows = query[1]
        
        # Find the best blow that reduces heads maximally
        best_reduction = 0
        best_growth = float('inf')
        
        for d, h in blows:
            best_reduction = max(best_reduction, d)
            if d < x:  # Only consider growing heads if we can reduce heads
                best_growth = min(best_growth, h)
        
        if best_reduction <= best_growth:
            # If the best reduction is less than or equal to growth, we can't win
            results.append(-1)
            continue
        
        # Calculate the number of blows needed
        blows_required = 0
        while x > 0:
            blows_required += 1
            x -= best_reduction
            if x > 0:
                x += best_growth
        
        results.append(blows_required)
    
    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append(((n, x), blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Print results
for result in results:
    print(result)