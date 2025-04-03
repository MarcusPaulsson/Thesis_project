def min_blows_to_defeat_zmei(t, queries):
    results = []
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                # Can defeat with this blow in one hit
                min_blows = min(min_blows, 1)
                possible = True
            else:
                # Calculate the effective decrease in heads after the blow
                effective_decrease = d - h
                if effective_decrease < 0:
                    continue  # This blow is not effective
                # Calculate how many blows needed
                blows_needed = (x - d + effective_decrease - 1) // effective_decrease + 1
                min_blows = min(min_blows, blows_needed)
                possible = True
        
        results.append(min_blows if possible else -1)
    
    return results

# Example usage
t = 3
queries = [
    (3, 10, [(6, 3), (8, 2), (1, 4)]),
    (4, 10, [(4, 1), (3, 2), (2, 6), (1, 100)]),
    (2, 15, [(10, 11), (14, 100)])
]

results = min_blows_to_defeat_zmei(t, queries)
for result in results:
    print(result)