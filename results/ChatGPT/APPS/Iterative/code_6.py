def min_blows_to_defeat(t, queries):
    results = []
    
    for i in range(t):
        n, x = queries[i][0], queries[i][1]
        blows = queries[i][2]
        
        min_blow = float('inf')
        max_effective_d = 0
        
        for d, h in blows:
            if d >= x:
                # If d is greater than or equal to x, it can defeat Zmei in one blow
                min_blow = 1
                break
            else:
                # Calculate the effective reduction in heads
                effective_d = d - h
                if effective_d > 0:
                    max_effective_d = max(max_effective_d, effective_d)
        
        if min_blow == 1:
            results.append(1)
            continue
        
        if max_effective_d <= 0:
            results.append(-1)
            continue
        
        # Calculate the number of blows needed
        blows_needed = (x - max_effective_d + max_effective_d - 1) // max_effective_d
        
        results.append(blows_needed + 1)  # +1 for the blow that will take it to zero
    
    return results

# Input reading and function call
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

results = min_blows_to_defeat(t, queries)
for result in results:
    print(result)