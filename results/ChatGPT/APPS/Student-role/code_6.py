def min_blows_to_defeat_zmei(t, queries):
    results = []

    for i in range(t):
        n, x = queries[i][0]
        blows = queries[i][1]
        
        min_blow_count = float('inf')
        can_defeat = False
        
        for d, h in blows:
            if d >= x:
                # If this blow can defeat Zmei in one hit
                min_blow_count = 1
                can_defeat = True
                break
            
            # Calculate the effective reduction after one blow
            heads_after_blow = x - d + h
            
            # If still has heads after the blow
            if heads_after_blow > 0:
                # Calculate how many blows are needed to ultimately defeat Zmei
                effective_heads_to_defeat = heads_after_blow
                blows_needed = 1  # We already used 1 blow
                
                # Calculate how many more blows are needed
                while effective_heads_to_defeat > 0:
                    effective_heads_to_defeat -= d
                    if effective_heads_to_defeat > 0:
                        effective_heads_to_defeat += h
                    blows_needed += 1
                
                min_blow_count = min(min_blow_count, blows_needed)
                can_defeat = True
        
        if can_defeat:
            results.append(min_blow_count)
        else:
            results.append(-1)
    
    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append(((n, x), blows))

# Calculate results
results = min_blows_to_defeat_zmei(t, queries)

# Output results
for result in results:
    print(result)