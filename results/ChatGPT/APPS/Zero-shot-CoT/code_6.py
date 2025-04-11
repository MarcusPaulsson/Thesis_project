def min_blows_to_defeat_zmei(t, queries):
    results = []
    for query in queries:
        n, x, blows = query
        min_blow_count = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                # If we can defeat Zmei Gorynich in one blow
                min_blow_count = min(min_blow_count, 1)
                possible = True
            else:
                # Calculate the effective heads after one blow
                effective_heads = x - d + h
                if effective_heads > 0:
                    # Calculate how many blows are needed to reduce heads to 0
                    # We need to reduce effective_heads to 0
                    # Each blow reduces by d and adds h
                    # So we need to find how many blows are needed
                    blows_needed = (effective_heads + (d - h) - 1) // (d - h) + 1
                    min_blow_count = min(min_blow_count, blows_needed)
                    possible = True
        
        if possible:
            results.append(min_blow_count)
        else:
            results.append(-1)
    
    return results

# Example usage:
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

results = min_blows_to_defeat_zmei(t, queries)
for result in results:
    print(result)