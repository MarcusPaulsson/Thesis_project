def min_blows_to_defeat(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')

        for d_i, h_i in blows:
            if d_i >= x:
                min_blows = min(min_blows, 1)
            else:
                effective_heads_lost = d_i - h_i
                if effective_heads_lost <= 0:
                    continue
                blows_needed = (x - d_i + effective_heads_lost - 1) // effective_heads_lost + 1
                min_blows = min(min_blows, blows_needed)

        results.append(min_blows if min_blows != float('inf') else -1)

    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Process and output results
results = min_blows_to_defeat(t, queries)
for result in results:
    print(result)