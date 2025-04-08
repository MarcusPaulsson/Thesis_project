def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x = query[0]
        blows = query[1]
        
        min_blow_needed = float('inf')
        can_defeat = False
        
        for d, h in blows:
            effective_damage = d - h
            
            # If the blow can defeat Zmei in one hit
            if d >= x:
                min_blow_needed = min(min_blow_needed, 1)
                can_defeat = True
                continue
            
            # If the blow is ineffective (no reduction in heads or worse)
            if effective_damage <= 0:
                continue
            
            # Calculate the number of blows needed to reduce heads to zero
            blows_needed = (x + effective_damage - 1) // effective_damage
            min_blow_needed = min(min_blow_needed, blows_needed)
            can_defeat = True
            
        results.append(min_blow_needed if can_defeat else -1)
    
    return results

# Example usage
t = 3
queries = [
    ((3, 10), [(6, 3), (8, 2), (1, 4)]),
    ((4, 10), [(4, 1), (3, 2), (2, 6), (1, 100)]),
    ((1, 100), [(2, 15), (10, 11), (14, 100)])
]

results = min_blows_to_defeat_zmei(t, queries)
for res in results:
    print(res)