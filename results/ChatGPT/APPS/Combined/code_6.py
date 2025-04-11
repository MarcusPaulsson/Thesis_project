def min_blows_to_defeat_zmei(t, queries):
    results = []
    
    for n, x, blows in queries:
        # Initialize the best blow variables
        best_d = 0
        best_h = float('inf')
        
        # Find the best blow
        for d, h in blows:
            if d > best_d:
                best_d = d
                best_h = h
            elif d == best_d:
                best_h = min(best_h, h)
        
        # If the best blow can defeat Zmei Gorynich in one hit
        if best_d >= x:
            results.append(1)
            continue
        
        # If the best blow does not reduce heads effectively
        if best_h >= best_d:
            results.append(-1)
            continue
        
        # Calculate the number of blows needed
        blows_needed = 0
        while x > 0:
            blows_needed += 1
            x -= best_d
            if x > 0:
                x += best_h
        
        results.append(blows_needed)
    
    return results

# Input reading
t = int(input())
queries = []

for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results and print
results = min_blows_to_defeat_zmei(t, queries)
for result in results:
    print(result)