def min_cost_to_break_chocolate(t, queries):
    results = []
    for n, m, k in queries:
        total_squares = n * m
        if k == total_squares:
            results.append(0)
            continue
        
        min_cost = float('inf')
        
        for eat in range(1, k + 1):
            remaining = total_squares - eat
            
            # Break vertically
            for i in range(1, n):
                cost = m * m
                cost += min_cost_to_break_chocolate(t, [(i, m, eat)])  # top part
                cost += min_cost_to_break_chocolate(t, [(n - i, m, remaining)])  # bottom part
                min_cost = min(min_cost, cost)
            
            # Break horizontally
            for j in range(1, m):
                cost = n * n
                cost += min_cost_to_break_chocolate(t, [(n, j, eat)])  # left part
                cost += min_cost_to_break_chocolate(t, [(n, m - j, remaining)])  # right part
                min_cost = min(min_cost, cost)

        results.append(min_cost)
    
    return results

# Input reading
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
results = min_cost_to_break_chocolate(t, queries)

# Output results
for result in results:
    print(result)