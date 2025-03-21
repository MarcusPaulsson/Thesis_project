def solve():
    n = int(input())
    triangles = []
    for _ in range(n - 2):
        triangles.append(list(map(int, input().split())))

    def check_permutation(p):
        adj = {i: [] for i in range(1, n + 1)}
        for i in range(n):
            adj[p[i]].append(p[(i - 1 + n) % n])
            adj[p[i]].append(p[(i + 1) % n])
        
        cut_order = []
        remaining_triangles = list(range(n - 2))
        
        while remaining_triangles:
            found = False
            for i in list(remaining_triangles):
                triangle = triangles[i]
                
                valid = True
                for v in triangle:
                    count = 0
                    for neighbor in adj[v]:
                        if neighbor in triangle:
                            count += 1
                    if count < 2:
                        valid = False
                        break
                
                if valid:
                    cut_order.append(i + 1)
                    remaining_triangles.remove(i)
                    
                    for v in triangle:
                        for neighbor in triangle:
                            if neighbor != v and neighbor in adj[v]:
                                adj[v].remove(neighbor)
                    
                    found = True
                    break
            
            if not found:
                return False, []
        
        return True, cut_order

    import itertools
    for p in itertools.permutations(range(1, n + 1)):
        success, cut_order = check_permutation(list(p))
        if success:
            print(*p)
            print(*cut_order)
            return

t = int(input())
for _ in range(t):
    solve()