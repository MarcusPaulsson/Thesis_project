def can_win_2048(queries):
    results = []
    for query in queries:
        n, s = query
        # Check if 2048 is already in the multiset
        if 2048 in s:
            results.append("YES")
            continue
        
        # Sum up all the powers of two less than or equal to 2048
        total = sum(x for x in s if x < 2048)
        
        # If the total is at least 2048, we can form it
        if total >= 2048:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    queries.append((n, s))

# Get results
results = can_win_2048(queries)

# Print the results
for result in results:
    print(result)