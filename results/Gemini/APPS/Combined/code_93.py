def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1:
        if n > 2 or k == 1:
            print("NO")
        else:
            print("YES")
            print("1 2")
        return

    if k == 1:
        print("NO")
        return

    if d >= n:
        print("NO")
        return

    if d > n - 1:
        print("NO")
        return

    if d > 1 and k == 1:
        print("NO")
        return
    
    if n > 2 and d == 1 and k == 1:
        print("NO")
        return

    if d > 2 and k == 2:
        print("NO")
        return
    
    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))

    next_node = d + 2
    
    # Add nodes to the diameter path
    for i in range(1, d + 2):
        while next_node <= n:
            degree = 0
            for u, v in edges:
                if u == i or v == i:
                    degree += 1
            
            if degree < k:
                edges.append((i, next_node))
                next_node += 1
            else:
                break
        if next_node > n:
            break
    
    if next_node <= n:
        print("NO")
        return

    if len(edges) != n - 1:
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        print(u, v)

solve()