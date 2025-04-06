def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        print("NO")
        return

    if k == 1 and d > 1:
        print("NO")
        return

    if k == 1 and d == 1 and n > 2:
        print("NO")
        return
    
    if k == 1 and d == 1 and n == 2:
        print("YES")
        print("1 2")
        return

    edges = []
    nodes = [i for i in range(1, n + 1)]

    # Construct the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))

    nodes_used = d + 1
    
    if k < 2:
        if n > d + 1 : print("NO")
        else:
            print("YES")
            for u, v in edges:
                print(u,v)
        return

    # Add remaining nodes as leaves to the diameter path
    current_node = d+2
    for i in range(1,d+1):
      
      while current_node <= n:
        if len([e for u,v in edges if u==i or v==i]) < k:
          edges.append((i,current_node))
          current_node +=1
        else:
          break

    if current_node <= n:
        print("NO")
        return

    print("YES")
    for edge in edges:
        print(edge[0], edge[1])


solve()