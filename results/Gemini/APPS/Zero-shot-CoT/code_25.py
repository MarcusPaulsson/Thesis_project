def solve():
    n = int(input())
    triangles = []
    for _ in range(n - 2):
        triangles.append(list(map(int, input().split())))

    def check_permutation(permutation, triangle_order):
        adj = [[] for _ in range(n + 1)]
        for i in range(n):
            adj[permutation[i]].append(permutation[(i + 1) % n])
            adj[permutation[(i + 1) % n]].append(permutation[i])

        for triangle_index in triangle_order:
            a, b, c = triangles[triangle_index - 1]
            
            a_index = permutation.index(a)
            b_index = permutation.index(b)
            c_index = permutation.index(c)
            
            indices = sorted([a_index, b_index, c_index])

            if indices[1] - indices[0] == 1 and indices[2] - indices[1] == 1:
                
                new_adj = [[] for _ in range(n + 1)]
                for i in range(n):
                    if permutation[i] not in [a,b,c]:
                        new_adj[permutation[i]].append(permutation[(i + 1) % n])
                        new_adj[permutation[(i + 1) % n]].append(permutation[i])
                
                
                
                if a in adj[b] and b in adj[a]:
                    adj[a].remove(b)
                    adj[b].remove(a)
                if a in adj[c] and c in adj[a]:
                    adj[a].remove(c)
                    adj[c].remove(a)
                if b in adj[c] and c in adj[b]:
                    adj[b].remove(c)
                    adj[c].remove(b)
                    
               
                
                continue
            elif indices[0] == 0 and indices[1] == 1 and indices[2] == n-1:
                
                new_adj = [[] for _ in range(n + 1)]
                for i in range(n):
                    if permutation[i] not in [a,b,c]:
                        new_adj[permutation[i]].append(permutation[(i + 1) % n])
                        new_adj[permutation[(i + 1) % n]].append(permutation[i])
                
                if a in adj[b] and b in adj[a]:
                    adj[a].remove(b)
                    adj[b].remove(a)
                if a in adj[c] and c in adj[a]:
                    adj[a].remove(c)
                    adj[c].remove(a)
                if b in adj[c] and c in adj[b]:
                    adj[b].remove(c)
                    adj[c].remove(b)
                    
                
                continue
            else:
                
                return False
        return True

    import itertools
    for permutation in itertools.permutations(range(1, n + 1)):
        permutation = list(permutation)
        
        for triangle_order in itertools.permutations(range(1, n - 1 + 1)):
            triangle_order = list(triangle_order)
            
            if check_permutation(permutation, triangle_order):
                print(*permutation)
                print(*triangle_order)
                return

    for permutation in itertools.permutations(range(1, n + 1)):
        permutation = list(permutation)
        permutation = permutation[::-1]

        for triangle_order in itertools.permutations(range(1, n - 1 + 1)):
            triangle_order = list(triangle_order)
            
            if check_permutation(permutation, triangle_order):
                print(*permutation)
                print(*triangle_order)
                return



t = int(input())
for _ in range(t):
    solve()