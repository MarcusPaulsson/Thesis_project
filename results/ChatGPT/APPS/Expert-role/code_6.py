def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        
        for d, h in blows:
            if d >= x:
                min_blows = min(min_blows, 1)
            else:
                # Calculate the effective heads after one blow
                effective_heads = x - d + h
                if effective_heads <= 0:
                    min_blows = min(min_blows, 1)
                else:
                    # Calculate how many blows are needed to bring heads to 0
                    # We need to reduce effective_heads to 0
                    # Each blow reduces by d and adds h
                    # So we need to find the number of blows needed
                    # Let k be the number of blows
                    # effective_heads - k * h <= 0
                    # k * d >= effective_heads
                    # k >= effective_heads / d
                    # k >= (effective_heads + h - 1) // h (to round up)
                    # k >= (effective_heads + d - 1) // d (to round up)
                    k = (effective_heads + d - 1) // d
                    min_blows = min(min_blows, k + 1)
        
        results.append(min_blows if min_blows != float('inf') else -1)
    
    return results

# Input reading
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