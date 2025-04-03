def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x, blows = query
        min_blow = float('inf')
        
        for d, h in blows:
            if d >= x:
                min_blow = 1
            else:
                # Calculate the effective reduction and growth
                net_change = d - h
                if net_change <= 0:
                    continue  # This blow can never reduce the heads effectively
                
                # Calculate how many blows are needed
                blows_needed = (x - d + net_change - 1) // net_change + 1
                min_blow = min(min_blow, blows_needed)
        
        results.append(min_blow if min_blow != float('inf') else -1)
    
    return results

# Example usage:
t = 3
queries = [
    (3, 10, [(6, 3), (8, 2), (1, 4)]),
    (4, 10, [(4, 1), (3, 2), (2, 6), (1, 100)]),
    (2, 15, [(10, 11), (14, 100)])
]

results = min_blows_to_defeat_zmei(t, queries)
for result in results:
    print(result)