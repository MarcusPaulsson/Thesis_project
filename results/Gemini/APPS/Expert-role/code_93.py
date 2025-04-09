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
      
    if k == 1 and d == 0 and n == 1:
      print("YES")
      return

    edges = []
    degrees = [0] * (n + 1)

    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
        degrees[i + 1] += 1
        degrees[i + 2] += 1

    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    next_node = d + 2
    
    # Add remaining nodes
    for i in range(1, n + 1):
      if next_node > n:
        break
      
      if degrees[i] < k:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            next_node += 1
            
            
    for i in range(1, n + 1):
      if next_node > n:
        break
      
      if degrees[i] < k:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            next_node += 1

    if len(edges) != n - 1:
        print("NO")
        return

    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()