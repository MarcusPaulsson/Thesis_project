def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def is_safe(closed_spots):
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for u, v in edges:
            if u not in closed_spots and v not in closed_spots:
                adj[u].append(v)

        for start_node in range(1, n + 1):
            if start_node in closed_spots:
                continue
            
            q = [(start_node, [start_node])]
            
            while q:
                curr_node, path = q.pop(0)
                
                if len(path) > 1:
                    return False
                
                for neighbor in adj[curr_node]:
                    q.append((neighbor, path + [neighbor]))

        return True

    for i in range(1 << n):
        closed_spots = []
        for j in range(n):
            if (i >> j) & 1:
                closed_spots.append(j + 1)
        
        if len(closed_spots) <= (4/7) * n:
            if is_safe(closed_spots):
                print(len(closed_spots))
                print(*closed_spots)
                return

t = int(input())
for _ in range(t):
    solve()