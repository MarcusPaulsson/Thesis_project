def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for query in queries:
        n, x = query[0]
        blows = query[1]
        
        # Initialize variables to track the best blow options
        max_d = 0
        min_h = float('inf')
        
        for d, h in blows:
            max_d = max(max_d, d)
            if d < x:
                min_h = min(min_h, h)
        
        # If the maximum damage can defeat Zmei in one blow
        if max_d >= x:
            results.append(1)
            continue
        
        # If there's no blow that can reduce heads effectively
        if min_h == float('inf'):
            results.append(-1)
            continue
        
        # Calculate the number of blows needed
        blows_needed = 0
        while x > 0:
            blows_needed += 1
            x -= max_d
            if x > 0:
                x += min_h
        
        results.append(blows_needed)
    
    return results

# Input reading
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append(((n, x), blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Output results
for result in results:
    print(result)