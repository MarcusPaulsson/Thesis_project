def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blow_count = float('inf')
        
        for d, h in blows:
            if d >= x:
                min_blow_count = min(min_blow_count, 1)
            elif h >= d:
                continue  # This blow is not effective as it grows more heads than it cuts
            else:
                # Calculate the effective reduction per blow
                effective_reduction = d - h
                # Calculate the number of blows needed
                blows_needed = (x - d + effective_reduction - 1) // effective_reduction + 1
                min_blow_count = min(min_blow_count, blows_needed)
        
        results.append(min_blow_count if min_blow_count != float('inf') else -1)
    
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