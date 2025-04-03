def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k < 2:
            print("NO")
            return
        
    if d > 1 and k == 1:
        print("NO")
        return
    
    if d > 1 and k == 2 and n > d+1:
        print("NO")
        return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    available_nodes = list(range(1, n + 1))
    
    # Remove nodes used in the diameter
    diameter_nodes = set(range(1, d + 2))
    remaining_nodes = []
    for node in available_nodes:
        if node not in diameter_nodes:
            remaining_nodes.append(node)
    
    # Add nodes to the diameter path
    current_diameter_node_index = 1
    for node in remaining_nodes:
        while degrees[current_diameter_node_index] >= k:
            current_diameter_node_index += 1
            if current_diameter_node_index > d + 1:
                print("NO")
                return

        edges.append((current_diameter_node_index, node))
        degrees[current_diameter_node_index] += 1
        degrees[node] += 1

    print("YES")
    for u, v in edges:
        print(u, v)

solve()