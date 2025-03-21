def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    for closed_spots_count in range(n + 1):
        for i in range(1 << n):
            if bin(i).count('1') != closed_spots_count:
                continue

            closed_spots = []
            for j in range(n):
                if (i >> j) & 1:
                    closed_spots.append(j + 1)

            
            valid = True
            
            
            adj = [[] for _ in range(n + 1)]
            for u, v in edges:
              if u not in closed_spots and v not in closed_spots:
                adj[u].append(v)

            
            
            def has_path_length_2_or_more(start_node):
              
              visited = set()
              q = [(start_node, 0)] 
              
              while q:
                node, path_len = q.pop(0)
                
                if node in visited:
                  continue
                visited.add(node)
                
                if path_len >= 2:
                  return True
                
                for neighbor in adj[node]:
                  q.append((neighbor, path_len + 1))
              return False
            

            
            safe = True
            for start_node in range(1, n + 1):
                if start_node not in closed_spots:
                    if has_path_length_2_or_more(start_node):
                      safe = False
                      break
            
            if safe:
                if closed_spots_count <= (4/7) * n:
                  print(len(closed_spots))
                  print(*closed_spots)
                  return
            
T = int(input())
for _ in range(T):
    solve()