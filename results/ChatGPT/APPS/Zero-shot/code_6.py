def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x = query[0]
        blows = query[1]
        
        min_blow_count = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                min_blow_count = 1
                possible = True
                break
            
            effective_d = d - h
            if effective_d > 0:
                blows_needed = (x - d + effective_d - 1) // effective_d + 1
                min_blow_count = min(min_blow_count, blows_needed)
                possible = True
        
        results.append(min_blow_count if possible else -1)
    
    return results

# Reading input
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append(((n, x), blows))

# Getting results
results = min_blows_to_defeat_zmei(t, queries)

# Outputting results
for result in results:
    print(result)