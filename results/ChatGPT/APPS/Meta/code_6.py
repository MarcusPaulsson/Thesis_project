def min_blows_to_defeat_zmei(t, queries):
    results = []
    for i in range(t):
        n, x = queries[i][0]
        blows = queries[i][1]
        
        # Initialize variables to track the best blow options
        max_d = 0
        min_h = float('inf')
        
        for d, h in blows:
            max_d = max(max_d, d)
            if d < x:  # Only consider blows that can be useful when current heads are > d
                min_h = min(min_h, h)

        # If we can't cut off more heads than we have, we need to check the growth
        if max_d < min_h:
            results.append(-1)
            continue
        
        # Calculate the minimum number of blows required
        blows_count = 0
        while x > 0:
            if max_d >= x:
                blows_count += 1  # One blow to defeat
                break
            else:
                blows_count += 1
                x = x - max_d + min_h
            
        results.append(blows_count)
    
    return results

# Example usage:
t = 3
queries = [
    ((3, 10), [(6, 3), (8, 2), (1, 4)]),
    ((4, 10), [(4, 1), (3, 2), (2, 6), (1, 100)]),
    ((1, 100), [(2, 15), (10, 11), (14, 100)])
]

results = min_blows_to_defeat_zmei(t, queries)
for res in results:
    print(res)