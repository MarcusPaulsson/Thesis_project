def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k <= 1:
            print("NO")
            return
    if d == 1 and n == 2 and k < 1:
        print("NO")
        return

    if d > 1 and k == 1:
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))

    remaining_nodes = n - (d + 1)
    
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    available_nodes = list(range(1, n + 1))
    
    def find_node_with_degree_less_than_k():
        for node in available_nodes:
            if degrees[node] < k:
                return node
        return None
    
    current_node_index = 1
    
    for _ in range(remaining_nodes):
        node_to_connect = find_node_with_degree_less_than_k()
        if node_to_connect is None:
            print("NO")
            return
        
        new_node = len(degrees)
        while new_node in available_nodes:
          new_node += 1
        
        
        if new_node > n:
          
          new_node = 0
          for i in range(1, n+1):
            
            if i not in [node[0] for node in edges]:
                
                new_node = i
                break
          
          if new_node == 0:
            print("NO")
            return

        edges.append((node_to_connect, current_node_index + d +1))
        degrees[node_to_connect] += 1
        degrees[current_node_index + d + 1] = 1
        current_node_index += 1
    
    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        print(u, v)

solve()