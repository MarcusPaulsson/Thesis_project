def can_transform(q, queries):
    results = []
    for i in range(q):
        s = queries[i][0]
        t = queries[i][1]
        
        if s == t:
            results.append("YES")
            continue
        
        # Check if both strings have at least one common character
        common_characters = set(s) & set(t)
        
        if common_characters:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
q = int(input())
queries = [tuple(input().strip() for _ in range(2)) for _ in range(q)]

# Get results
results = can_transform(q, queries)

# Print results
for result in results:
    print(result)