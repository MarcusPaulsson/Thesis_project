def construct_tree(n, d, k):
    # Step 1: Check for impossible conditions
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > k + 1 and d == 1):
        return "NO"
    
    # Step 2: Initialize the tree structure
    edges = []
    
    # Step 3: Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Step 4: Add additional nodes to maintain the degree constraint
    current_node = d + 2
    for i in range(1, d + 1):
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_node <= n:
            edges.append((i, current_node))
            current_node += 1
            if current_node > n:
                break
    
    # Step 5: Check if we have used all nodes
    if current_node <= n:
        return "NO"
    
    # Step 6: Return the result
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(result)

# Input reading
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))