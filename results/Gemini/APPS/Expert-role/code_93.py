def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return
    
    if d == 1 and n > 2:
        print("NO")
        return

    if k == 1 and n > 2:
        print("NO")
        return
    
    if d > n - 1:
       print("NO")
       return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    remaining_nodes = list(range(d + 2, n + 1))
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
        
    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    # Add nodes to the diameter path
    current_node = d + 2
    
    for i in range(1, d + 2):
        while degrees[i] < k and remaining_nodes:
            edges.append((i, remaining_nodes[0]))
            degrees[i] += 1
            degrees[remaining_nodes[0]] += 1
            remaining_nodes.pop(0)
            
    if remaining_nodes:
        print("NO")
        return

    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    if len(edges) != n - 1:
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        print(u, v)

solve()