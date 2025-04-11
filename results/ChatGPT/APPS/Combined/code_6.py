def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for n, x, blows in queries:
        min_blows = float('inf')
        
        for d, h in blows:
            if d >= x:
                min_blows = min(min_blows, 1)
            else:
                effective_damage = d - h
                if effective_damage > 0:
                    blows_needed = (x - d + effective_damage - 1) // effective_damage + 1
                    min_blows = min(min_blows, blows_needed)
        
        results.append(min_blows if min_blows != float('inf') else -1)
    
    return results