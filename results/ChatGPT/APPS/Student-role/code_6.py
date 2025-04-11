def min_blows_to_defeat(t, queries):
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
                if effective_heads > 0:
                    # Calculate the number of blows needed
                    blows_needed = (effective_heads + (d - h) - 1) // (d - h) + 1
                    min_blows = min(min_blows, blows_needed)
        
        results.append(min_blows if min_blows != float('inf') else -1)
    
    return results

# Input reading and function calling
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

results = min_blows_to_defeat(t, queries)
for result in results:
    print(result)