def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x = query[0], query[1]
        blows = query[2]
        
        # Find the best blow
        best_d = 0
        best_h = 0
        
        for d, h in blows:
            if d > best_d:
                best_d = d
                best_h = h
            elif d == best_d and h < best_h:
                best_h = h
        
        if best_d == 0:
            results.append(-1)
            continue
        
        blows_needed = 0
        
        while x > 0:
            blows_needed += 1
            if best_d >= x:
                x = 0
            else:
                x = x - best_d + best_h
        
            if x < 0:
                x = 0
        
        results.append(blows_needed)
    
    return results

# Reading input
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