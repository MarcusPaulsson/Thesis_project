def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for n, x, blows in queries:
        min_blows = float('inf')
        possible = False
        
        for d, h in blows:
            if d >= x:
                # If we can defeat Zmei in one blow
                min_blows = min(min_blows, 1)
                possible = True
            else:
                # Calculate the effective reduction after one blow
                effective_heads = x - d + h
                if effective_heads < x:
                    # Calculate how many blows are needed to bring heads to 0
                    blows_needed = (x - d + h - 1) // (h - d) + 1
                    min_blows = min(min_blows, blows_needed)
                    possible = True
        
        results.append(min_blows if possible else -1)
    
    return results