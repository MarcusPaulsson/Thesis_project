def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k <= 1:
            print("NO")
            return
        
        if n > k:
            print("NO")
            return

    if d > 1 and k == 1:
        print("NO")
        return


    edges = []
    nodes = list(range(1, n + 1))

    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    used_nodes = set(range(1, d + 2))

    # Add remaining nodes as leaves
    for i in range(1, d + 2):
        while True:
            if len(used_nodes) == n:
                break

            count = 0
            for u, v in edges:
                if u == i or v == i:
                    count += 1
            
            if count >= k:
                break

            
            next_node = -1
            for node in nodes:
                if node not in used_nodes:
                    next_node = node
                    break

            if next_node == -1:
                break
                
            edges.append((i, next_node))
            used_nodes.add(next_node)
            

    if len(edges) != n - 1 or len(used_nodes) != n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()